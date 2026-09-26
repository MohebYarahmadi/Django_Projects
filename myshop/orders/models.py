from django.conf import settings
from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator

from coupons.models import Coupon

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stripe_id = models.CharField(max_length=250, blank=True)
    is_paid = models.BooleanField(default=False)

    coupon = models.ForeignKey(Coupon, null=True, blank=True, on_delete=models.SET_NULL, related_name='orders')
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def get_total_cost(self):
        total_cost = self.get_total_const_before_discount()
        return total_cost - self.get_discount()

    def get_stripe_url(self):
        if not self.stripe_id:
            # no payment associated
            return ''
        if '_test_' in settings.STRIPE_SECRET_KEY:
            # stripe path for test payment
            path = '/test/'
        else:
            # stripe path for real payment
            path = '/'
        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'

    def get_total_const_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_discount(self):
        total_cost = self.get_total_const_before_discount()
        if self.discount:
            return total_cost * (self.discount / Decimal(100))
        return Decimal(0)

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='order_items')

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return str(self.id)
