from django.contrib.auth.views import LoginView
from django.urls import path
from apps.views import IndexListView, ProfileTemplateView, RegisterCreateView, ProductDetailView

urlpatterns = [
    path('', IndexListView.as_view(), name='list_view'),
    path('profile', ProfileTemplateView.as_view(), name='profile_page'),
    path('login', LoginView.as_view(
        template_name='apps/auth/login.html',
        next_page='profile_page',
        redirect_authenticated_user=True,
    ), name='login_page'),
    path('register', RegisterCreateView.as_view(), name='register_page'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail_view'),
]
