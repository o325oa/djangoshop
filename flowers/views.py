from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'flowers/home.html')

def catalog(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'flowers/catalog.html', {'products': products})

def about(request):
    return render(request, 'flowers/about.html')