from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, Model, CharField, ForeignKey, CASCADE, DateTimeField, ManyToManyField
from django_ckeditor_5.fields import CKEditor5Field


class User(AbstractUser):
    photo = ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)


class Tag(Model):
    name = CharField(max_length=50)


class Category(Model):
    name = CharField(max_length=255)


class Blog(Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to='blogs/%Y/%m/%d/')
    description = CKEditor5Field(null=True, blank=True)
    author = ForeignKey('apps.User', CASCADE)
    category = ForeignKey('apps.Category', CASCADE)
    tags = ManyToManyField('apps.Tag', blank=True)
    created_at = DateTimeField(auto_now_add=True)
