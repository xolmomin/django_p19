from django.contrib import admin

from apps.models import Category, Product, Region, District


@admin.register(Region)
class RegionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(District)
class DistrictModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['name', 'id']
    search_fields = ['name', 'description']
