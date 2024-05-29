from rest_framework import serializers
from rest_framework.fields import SlugField
from rest_framework.serializers import ModelSerializer

from apps.models import Course, User, Category


class CategoryModelSerializer(ModelSerializer):
    slug = SlugField(read_only=True)

    class Meta:
        model = Category
        fields = 'id', 'slug', 'name'


class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = 'id', 'title', 'video', 'price', 'category'


class UserUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'image'


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = 'password',
