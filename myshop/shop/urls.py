from django.urls import path

from . import views


app_name = 'shop'


urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('<slug:category_slug>/', views.product_list, name='product-list-by-category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product-detail'),
]
