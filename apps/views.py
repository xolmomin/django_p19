from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.models import Product, Category, Tag
from django.db.models import Q


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/list.html'

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        queryset = super().get_queryset()
        if tag:
            return queryset.filter(tags__in=[tag])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['tags'] = Tag.objects.all()
        return context


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'apps/detail.html'
    slug_url_kwarg = 'pk'

# def list_view(request):
#     # Product.objects.first()
#     # Product.objects.last()
#     # product o u
#     # products = Product.objects.filter(is_active=True)
#     # products = Product.objects.order_by('-title', 'created_at')
#     products = Product.objects.filter(Q(title__icontains='u') | Q(title__icontains='o'))
#     context = {
#         'blogs': products,
#         'tags': [],
#         'latest_blogs': [],
#     }
#     return render(request, 'apps/list.html', context)
#
#
# def detail_view(request, pk):
#     return render(request, 'apps/detail.html')
