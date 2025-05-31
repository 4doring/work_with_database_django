from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort', None)   
    phones = Phone.objects.all()
    match sort_param:
        case 'name': 
            phones = phones.order_by('name')
        case 'min_price':
            phones = phones.order_by('price')
        case 'max_price':
            phones = phones.order_by('-price')
        case _:
            phones = phones.order_by('-id')
            
    context = {
        'phones': phones,
        'current_sort': sort_param,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)