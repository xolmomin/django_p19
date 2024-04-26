from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView

from apps.models import Blog, Category


class BlogListView(ListView):
    queryset = Blog.objects.all()
    template_name = 'apps/blog/blog-list-left-sidebar.html'
    context_object_name = 'blogs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.prefetch_related('blog_set').annotate(blog_count=Count('blog__id'))
        # context['categories'] = Category.objects.all()
        return context


class BlogDetailView(DetailView):
    queryset = Blog.objects.all()
    template_name = 'apps/blog-details-left-sidebar.html'
    context_object_name = 'blog'


class CustomLoginView(LoginView):
    template_name = 'apps/auth/login.html'
    next_page = 'blog_list_page'


class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('blog_list_page')
