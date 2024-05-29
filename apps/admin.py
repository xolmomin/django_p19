from django.contrib import admin
from django.contrib.admin import action
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from apps.models import Course, User, Category, ModeratorUserProxy, StudentUserProxy, AdminUserProxy, TeacherUserProxy


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    filter_horizontal = 'students',
    autocomplete_fields = 'category',


class BaseUserAdmin(UserAdmin):
    list_display = 'id', 'first_name', 'show_image'
    filter_horizontal = ['groups', 'user_permissions']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("My photo"), {"fields": ("show_image", "image")}),
    )
    readonly_fields = ['show_image']

    def save_model(self, request, obj, form, change):
        obj.type = User.Type.MODERATOR
        obj.is_staff = True
        super().save_model(request, obj, form, change)

    @action(description='Rasm')
    def show_image(self, obj: User):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150px" height="150px" alt="">')
        return 'No image'


@admin.register(ModeratorUserProxy)
class ModeratorModelAdmin(BaseUserAdmin):

    def save_model(self, request, obj, form, change):
        obj.type = User.Type.MODERATOR
        super().save_model(request, obj, form, change)


@admin.register(AdminUserProxy)
class AdminModelAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Permissions"),
         {
             "fields": (
                 "is_active",
                 "is_staff",
                 "is_superuser",
                 "groups",
                 "user_permissions",
             ),
         },
         ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("My photo"), {"fields": ("show_image", "image")}),
    )

    def save_model(self, request, obj, form, change):
        obj.type = User.Type.ADMIN
        super().save_model(request, obj, form, change)


@admin.register(StudentUserProxy)
class StudentUserProxyModelAdmin(BaseUserAdmin):
    def save_model(self, request, obj, form, change):
        obj.type = User.Type.STUDENT
        super().save_model(request, obj, form, change)


@admin.register(TeacherUserProxy)
class TeacherUserProxyModelAdmin(BaseUserAdmin):
    def save_model(self, request, obj, form, change):
        obj.type = User.Type.TEACHER
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = 'name',
