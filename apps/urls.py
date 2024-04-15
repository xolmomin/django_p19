from django.urls import path
from apps.views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='list_view'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail_view'),
]
