from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, CreateView
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.
class IndexView(View):

    def get(self, request):
        context = {
            'title':'TEste',
            'texts':['dflksfkslk','sdfklsdlfçka']
        }
        return render(request, 'index.html',context)

index = IndexView.as_view()

'''
def index(request):
    context = {
        'title': 'Django Ecommerce HuehueBR',
        'texts': ['ajajj'],
        'category': Category.objects.all()
    }
    return render(request, "index.html", context=context)
'''

def contact(request):
    form = ContactForm(request.POST or None)
    success = False
    if request.method == 'POST':

        if form.is_valid():
            success = True
    else:
        form = ContactForm()

    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)


