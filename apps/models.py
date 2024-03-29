from django.db import models
from django.db.models import CASCADE
from django_ckeditor_5.fields import CKEditor5Field


class Region(models.Model):
    name = models.CharField(max_length=255)


class District(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey('apps.Region', CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = CKEditor5Field()
    image = models.ImageField(upload_to='products/', null=True)
    price = models.FloatField()
    category = models.ForeignKey('apps.Category', CASCADE)
