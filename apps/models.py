from django.contrib.auth.models import AbstractUser
from django.db.models import Model, DecimalField, SET_NULL, ForeignKey, CharField, DateTimeField, BooleanField, \
    ManyToManyField, TextField


class BaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(Model):
    name = CharField(max_length=50)


class Product(BaseModel):
    title = CharField(verbose_name='Nomi', max_length=255)
    description = TextField(null=True, blank=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    category = ForeignKey("apps.Category", SET_NULL, null=True, blank=True)
    tags = ManyToManyField("apps.Tag", related_name="products", blank=True)
    is_active = BooleanField(default=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'


class Order(BaseModel):
    name = CharField(verbose_name='Nomi', max_length=255)


class Tag(BaseModel):
    name = CharField(max_length=255)
