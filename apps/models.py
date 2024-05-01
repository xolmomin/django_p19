from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.postgres.fields import HStoreField
from django.db.models import ImageField, Model, CharField, ForeignKey, CASCADE, DateTimeField, ManyToManyField, \
    FloatField, TextField, JSONField, PositiveIntegerField
from django.utils.translation import gettext_lazy as _

from django_ckeditor_5.fields import CKEditor5Field


class User(AbstractUser):
    photo = ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    comments = GenericRelation('apps.Comment')

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class UserProxy(User):
    class Meta:
        proxy = True
        verbose_name = _('proxy_user')
        verbose_name_plural = _('proxy_users')


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
    comments = GenericRelation('apps.Comment')
    created_at = DateTimeField(auto_now_add=True)


class Product(Model):
    name = CharField(max_length=255)
    price = FloatField()
    image = ImageField(upload_to='products/%Y/%m')
    description = TextField(null=True, blank=True)
    info = JSONField(blank=True, null=True)
    comments = GenericRelation('apps.Comment')
    created_at = DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class Comment(Model):
    text = CharField(max_length=255)
    content_type = ForeignKey('contenttypes.ContentType', CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
