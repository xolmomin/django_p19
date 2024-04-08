from django.urls import path

from apps.views import index_menu_view, product_list_view, product_detail_view, form_view, profile_detail_view

urlpatterns = [
    path('', index_menu_view, name='index_menu_view'),
    path('product-list', product_list_view, name='product_list'),
    path('detail/<int:pk>', product_detail_view, name='product_detail'),
    # path('form', form_view, name='form_view'),
    path('form/<int:pk>', profile_detail_view, name='profile_detail_view'),
]
