from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Phone


def index(request):
    return redirect('catalog')


def get_phones(Phone):
    return [{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'release_date': p.release_date,
        'lte_exists': p.lte_exists,
        'slug': p.slug,
        'image': p.image,
        } for p in Phone.objects.all()] 


def show_catalog(request):
    template = 'catalog.html'
    sort_ = request.GET.get('sort', None)   
    phones = get_phones(Phone)
    match sort_:
        case 'name': 
            phones.sort(key=lambda i: i['name'])
        case 'min_price':
            phones.sort(reverse=False, key=lambda i: i['price'])
        case 'max_price':
            phones.sort(reverse=True, key=lambda i: i['price'])
            
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)