from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product
from .models import Category
# Create your views here.

class ProductListView(generic.ListView):

    #queryset = Product.objects.all()
    model = Product
    template_name = 'catalog/product_list.html'
    content_object_name = 'products'
    paginate_by = 2

product_list = ProductListView.as_view()

'''
def product_list(request):
    context = {
        'products':Product.objects.all()
    }
    return render(request, 'catalog/product_list.html',context=context)
'''



class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 1

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()
'''
def category(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'current_category': category.name,
        'product_list': products
    }

    return render(request, 'catalog/category.html', context)

'''
def product(request, slug):

    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)