from django.db import models

from api.surveysadmin.commons.models import (
    CommonFieldsModel,
    CommonOptionTypesModel,
    NameField,
)


# Create your models here.
class PoliticalSystemTypes(CommonOptionTypesModel):
    class Meta:
        db_table = "localization_political_system"
        verbose_name_plural = "Political System "

    def __str__(self) -> str:
        return f"{self.type_name}"


class Country(CommonFieldsModel):
    name = NameField(max_length=56, unique=True)
    iso_name_2 = models.CharField(max_length=2, unique=True)
    iso_name_3 = models.CharField(max_length=3, unique=True)
    phone_code = models.CharField(max_length=7, unique=True)
    political_system = models.ForeignKey(PoliticalSystemTypes, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self) -> str:
        return f"{self.name}"


class StateDepartment(CommonFieldsModel):

    name = NameField(max_length=56, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = "localization_state_department"
        verbose_name_plural = "States or Departments"

    def __str__(self) -> str:
        return f"{self.name}"


class City(CommonFieldsModel):

    name = NameField(max_length=56, unique=True)
    iso_name_2 = models.CharField(max_length=2, unique=True)
    iso_name_3 = models.CharField(max_length=3, unique=True)
    state_department = models.ForeignKey(StateDepartment, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self) -> str:
        return f"{self.name}"
