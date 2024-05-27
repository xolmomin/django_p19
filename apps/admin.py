from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.models import Course, User


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    filter_horizontal = 'users',


@admin.register(User)
class UserModelAdmin(UserAdmin):
    pass
