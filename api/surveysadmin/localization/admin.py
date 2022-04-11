from django.contrib import admin

# Register your models here.

from api.surveysadmin.localization.models import Country


@admin.register(Country)
class CompanyAdmin(admin.ModelAdmin):
    pass
