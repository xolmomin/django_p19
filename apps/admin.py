from django.contrib import admin

from apps.models import Advisor


@admin.register(Advisor)
class AdvisorModelAdmin(admin.ModelAdmin):
    pass
