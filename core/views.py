from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    texts = [
        'Lorem ipsum', 'dolor sit amet', 'consectetur'
    ]
    context = {
        'title':'Django Ecommerce HuehueBR',
        'texts':texts
    }
    return render(request, "index.html", context=context)

def contact(request):

    return render(request, 'contact.html')


def product_list(request):
    return render(request, 'product_list.html')


def product(request):
    return render(request, 'product.html')