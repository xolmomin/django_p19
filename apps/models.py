from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db.models import Model, CharField, FileField, IntegerField, ManyToManyField, ForeignKey, CASCADE


class User(AbstractUser):
    pass


class Category(Model):
    name = CharField(max_length=255)


class Course(Model):
    name = CharField(max_length=255)
    video = FileField(upload_to='course/', validators=[FileExtensionValidator(['mp4', 'webm'])])
    category = ForeignKey('apps.Category', CASCADE)
    price = IntegerField()
    users = ManyToManyField('apps.User', related_name='courses', blank=True)
