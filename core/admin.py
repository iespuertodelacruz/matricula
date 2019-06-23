from django.contrib import admin
from .models import EduLevel, Config


def clean_enrollment_dates(modeladmin, request, queryset):
    queryset.update(enrollment_date=None)


class EduLevelAdmin(admin.ModelAdmin):
    list_display = ['code', 'description', 'enrollment_date', 'cost']
    actions = [clean_enrollment_dates]


admin.site.register(EduLevel, EduLevelAdmin)


class ConfigAdmin(admin.ModelAdmin):
    pass


admin.site.register(Config, ConfigAdmin)
