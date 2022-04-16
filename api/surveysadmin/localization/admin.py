from django.contrib import admin

# Register your models here.

from api.surveysadmin.localization.models import Country, StateDepartment, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(StateDepartment)
class StateDepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class City(admin.ModelAdmin):
    pass
