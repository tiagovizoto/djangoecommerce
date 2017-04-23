from django.shortcuts import render
from .models import Product
from .models import Category
# Create your views here.


def product_list(request):
    context = {
        'products':Product.objects.all()
    }
    return render(request, 'catalog/product_list.html',context=context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'current_category': category.name,
        'product_list': products
    }

    return render(request, 'catalog/category.html', context)


def product(request, slug):

    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)