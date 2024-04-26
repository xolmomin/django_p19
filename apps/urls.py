from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import path

from apps.tasks import add, send_to_user_email
from apps.views import BlogListView, BlogDetailView, CustomLoginView, CustomLogoutView
from root import settings


def send_email_to_user(request):
    # add(2, 3)  # oddiy 5s
    # add.delay(2, 3)  # celery
    email = request.GET.get('email')
    msg = request.GET.get('msg')
    print(email, msg)
    send_to_user_email.delay(email, msg)
    # send_mail('Tema', 'xabar', settings.EMAIL_HOST_USER, [email])
    return HttpResponse('Hello, world')


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list_page'),
    path('blog-detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail_page'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('logout', CustomLogoutView.as_view(), name='logout_page'),
    path('send', send_email_to_user, name='logout_page'),
]

# crontab
# celery periodic
# apscheduler


