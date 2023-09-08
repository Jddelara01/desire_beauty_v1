from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to display all the products with sorting and searches """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
