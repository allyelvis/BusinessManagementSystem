from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Product, Order
from .forms import CustomerForm, ProductForm, OrderForm

def index(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'management/index.html', {'customers': customers, 'products': products, 'orders': orders})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'management/customer_detail.html', {'customer': customer})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'management/product_detail.html', {'product': product})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'management/order_detail.html', {'order': order})