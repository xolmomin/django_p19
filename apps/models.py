from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField


class User(AbstractUser):
    photo = ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
