from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    product_objects = Product.objects.all()
    # return render(request, "<h1>Hello world</h1>")
    return render(request, 'shop/index.html', {'product_objects': product_objects})
