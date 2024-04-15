from django.contrib import admin
from apps.models import Product, Category, Tag


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass
@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    pass
    # list_display = ['name', 'slug', 'custom_created_at']
    # readonly_fields = ['slug']
    #
    # @admin.display(description="O'zgarish vaqti")
    # def custom_created_at(self, obj: Product):
    #     return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')
    #
    # custom_created_at.short_description = "O'zgarish vaqti"
