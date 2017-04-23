from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category


# Create your views here.

def index(request):

    context = {
        'title':'Django Ecommerce HuehueBR',
        'texts':['ajajj'],
        'category':Category.objects.all()
    }
    return render(request, "index.html", context=context)


def contact(request):

    return render(request, 'contact.html')



