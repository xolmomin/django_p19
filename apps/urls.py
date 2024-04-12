from django.urls import path

from apps.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name='list_view'),
    path('detail/<int:pk>', detail_view, name='detail_view'),
]
