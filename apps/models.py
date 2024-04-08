from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True)


class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.TextField()
