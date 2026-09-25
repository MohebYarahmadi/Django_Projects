from cart.cart import Cart
from django.shortcuts import render, redirect

from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created


def order_create(request):
    template_name = ''
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
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
            # Launch asynchronous task
            order_created.delay(order.id)
            # Set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect('payment:process')
    else:
        form = OrderCreateForm()

    template_name = 'orders/order/create.html'
    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, template_name, context=context)
