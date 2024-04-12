from django.contrib import admin

from apps.models import Blog, Tag


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    pass
