# shop/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})
from django.shortcuts import render


def shop(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {'products': products})