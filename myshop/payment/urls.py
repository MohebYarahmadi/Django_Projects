from django.urls import path

from . import views


app_name = 'payment'


urlpatterns = [
    # Stripe
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    # Sandbox
    path('create/', views.create_payment, name='sandbox-create'),
    path('confirm/<string:intent_id>/', views.confirm_payment, name='sandbox-confirm'),
    path('refund/<string:intent_id>/', views.refund, name='sandbox-refund'),
    path('status/<string:intent_id>/', views.check_status, name='sandbox-status'),
]
