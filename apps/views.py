from django.shortcuts import render

from apps.models import Blog, Tag


def list_view(request):
    context = {
        'blogs': Blog.objects.all(),
        'tags': Tag.objects.all(),
        'latest_blogs': Blog.objects.order_by('-created_at')[:3],
    }

    return render(request, 'apps/list.html', context)


def detail_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog': blog,
        'tags': Tag.objects.all(),
        'latest_blogs': Blog.objects.order_by('-created_at')[:3],
    }
    return render(request, 'apps/detail.html', context)
