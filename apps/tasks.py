import time

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_to_user_email(email: str, message: str):
    print(email, message)
    send_mail('Tema', message, settings.EMAIL_HOST_USER, [email])
    return f'{email} ga yuborildi'


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
