# import uuid
#
# from django.core.validators import FileExtensionValidator
# from django.db import models
# from django.utils.text import slugify
# from django.utils.timezone import now
#
#
# class Product(models.Model):
#     class Type(models.TextChoices):
#         NEW = 'new', 'Yangi'
#         OLD = 'old', 'Eski'
#
#     name = models.CharField(verbose_name='Nomi', max_length=255)
#     slug = models.SlugField(max_length=255, unique=True)
#     type = models.CharField(max_length=5, choices=Type.choices, default=Type.NEW)
#     email = models.EmailField(default='test@mail.ru', db_index=True)
#     expire_at = models.DateField(verbose_name='Yaroqlilik muddati', default=now)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     ip = models.GenericIPAddressField(null=True, blank=True, help_text='IP manzilingizni kiriting')
#     image = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True,
#                               validators=[FileExtensionValidator(['png'])])
#     file = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True,
#                             validators=[FileExtensionValidator(['pdf'])], help_text='Faqat pdf yuklang')
#     json = models.JSONField(blank=True, default=dict, help_text='JSON malumot kiriting')
#     url = models.URLField(max_length=255, null=True, blank=True)
#     time = models.TimeField(default=now)
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True)
#
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         self.slug = slugify(self.name)
#         super().save(force_insert, force_update, using, update_fields)
#
#     class Meta:
#         ordering = ['']
#         indexes = [models.Index(fields=['slug'])]
#         index_together = []
#         unique_together = []
#         abstract = True
#         verbose_name = 'Mahsulot'
#         verbose_name_plural = 'Mahsulotlar'
from django.db.models import Model, DecimalField, SET_NULL, ForeignKey, CharField, DateTimeField, BooleanField, \
    ManyToManyField


class BaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(Model):
    name = CharField(max_length=50)


class Product(BaseModel):
    title = CharField(verbose_name='Nomi', max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    category = ForeignKey("apps.Category", SET_NULL, null=True, blank=True)
    tags = ManyToManyField("apps.Tag", related_name="products", blank=True)
    is_active = BooleanField(default=True)

    class Meta:
        db_table = 'mahsulot'
        ordering = ['-id']
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'


class Order(BaseModel):
    name = CharField(verbose_name='Nomi', max_length=255)


class Tag(BaseModel):
    name = CharField(max_length=255)
