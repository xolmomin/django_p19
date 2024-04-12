from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, TextField, DateTimeField, ImageField, ForeignKey, CASCADE, \
    ManyToManyField


class User(AbstractUser):
    image = ImageField(upload_to='images/')



class Tag(Model):
    name = CharField(max_length=255)


class Blog(Model):
    title = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='blogs/')
    author = ForeignKey('apps.User', CASCADE)
    tag = ManyToManyField('apps.Tag', blank=True)
    created_at = DateTimeField(auto_now_add=True)
