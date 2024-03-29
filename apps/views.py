from django.shortcuts import render

from apps.models import Category, Product


def index_view(request):
    products = Product.objects.order_by('id')[:2]
    context = {
        'products': products
    }
    return render(request, 'apps/index.html', context)


def detail_view(request):
    return render(request, 'apps/detail.html')

# databasedagi boshidagi 5tasini chiqaramiz
# 1-product name, price, category name

