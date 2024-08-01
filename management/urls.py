from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
]