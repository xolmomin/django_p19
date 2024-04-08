from django.contrib import admin

from apps.models import Profile


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    pass
