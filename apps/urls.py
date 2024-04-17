from django.urls import path
from apps.views import IndexListView, ProductListView, ProductDetailView

urlpatterns = [
    path('', IndexListView.as_view(), name='list_view'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail_view'),
]
