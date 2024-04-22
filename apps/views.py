from django.views.generic import TemplateView, DetailView


class IndexTemplateView(TemplateView):
    template_name = 'apps/shop-left-sidebar.html'


class DetailTemplateView(DetailView):
    queryset = ''
    template_name = 'apps/blog-details-left-sidebar.html'
