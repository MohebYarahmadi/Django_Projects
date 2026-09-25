from decimal import Decimal
import strip
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

import stripe_sandbox as sandbox  # or: import stripe as payment
from orders.models import Order



# Create the stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
string.api_version = settings.STRIPE_API_VERSION

sandbox.api_key = settings.STRIPE_SANDBOX_API_KEY
sandbox.api_base = settings.STRIPE_SANDBOX_API_BASE


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:conceled'))
        # Stripe checkout session data
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        # Add order items to the stripe checkout session
        for item in order.items.all():
            session_data['line_items'].append(
                {
                    'price_data': {
                        'unit_amount': int(item.price * Decimal('100')),
                        'currency': 'usd',
                        'product_data': {
                            'name': item.product.name,
                        },
                    },
                    'quantity': item.quantity,
                }
            )
        # Create stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        # Redirect to stripe payment form
        return redirect(session.url, code=303)

    else:
        return render(request, 'payment/process.html', locals())


def payment_completed(request):
    return render(request, 'payment/completed.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')



# ------------------------------- Sandbox --------------------------------------
def create_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    success_url = request.build_absolute_uri(reverse('payment:sandbox-status'))
    cancel_url = request.build_absolute_uri(reverse('payment:sandbox-status'))

    intent = sandbox.PaymentIntent.create(
        amount=2500,          # $25.00 (in cents)
        currency="usd",
        description="Order #{}".format(order.id),
        metadata={
            "order_id": str(order.id),
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        },
        receipt_email=request.user.email,
    )
    for item in order.items.all():
        intent['line_items'].append(
            {
                'price_data': {
                    'unit_amount': int(item.price * Decimal('100')),
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,
                    },
                },
                'quantity': item.quantity,
            }
        )
    return JsonResponse({"client_secret": intent.id, "id": intent.id})


def confirm_payment(request, intent_id):
    intent = sandbox.PaymentIntent.confirm(intent_id)
    # After confirm, the payment goes to "requires_action" (manual review).
    # Poll / retrieve to check if it was approved on the dashboard.
    return JsonResponse({"status": intent.status})


def check_status(request, intent_id):
    intent = sandbox.PaymentIntent.retrieve(intent_id)
    if intent.status == "succeeded":
        # Fulfill the order
        ...
    elif intent.status == "requires_action":
        # Still waiting for dashboard approval
        ...
    elif intent.last_payment_error:
        # Payment was denied
        return JsonResponse({"error": intent.last_payment_error.message})
    return JsonResponse({"status": intent.status})


def refund(request, intent_id):
    refund = sandbox.Refund.create(
        payment_intent=intent_id,
        reason="requested_by_customer",
    )
    return JsonResponse({"id": refund.id, "status": refund.status})
