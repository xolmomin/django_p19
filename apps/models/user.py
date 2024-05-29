from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField, TextChoices


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        STUDENT = 'student', 'Student'
        TEACHER = 'teacher', 'Teacher'

    type = CharField(max_length=255, choices=Type.choices, default=Type.STUDENT)
    image = ImageField(upload_to='users/images/', blank=True, null=True)
