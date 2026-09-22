from cart.cart import Cart
from django.shortcuts import render

from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    template_name = 'orders/order/created.html'
    cart = Cart(request)
    if request.method == 'POST':
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            # Clear the cart
            cart.clear()
            return render(request, template_name, { 'order': order })
    else:
        form = OrderCreateForm()

    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, template_name, context=context)
