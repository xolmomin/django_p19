from django.urls import path
from apps.views import IndexTemplateView, DetailTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='list_page'),
    path('detail/<id>', DetailTemplateView.as_view(), name='detail_page'),
]
