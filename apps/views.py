from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView, FormView, UpdateView, CreateView

from apps.forms import RegisterModelForm
from apps.models import Product, Category, Tag


class IndexListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/index.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        search = self.request.GET.get('search')
        queryset = Product.objects.all()
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        return context


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


class RegisterCreateView(CreateView):
    form_class = RegisterModelForm
    template_name = 'apps/auth/register.html'
    success_url = 'login'


class ProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/auth/profile.html'
    login_url = 'login_page'
