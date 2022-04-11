from django.db import models

from api.surveysadmin.commons.models import CommonModel


# Create your models here.
class Country(CommonModel):
    name = models.CharField(max_length=56, unique=True)
    iso_name_2 = models.CharField(max_length=2, unique=True)
    iso_name_3 = models.CharField(max_length=3, unique=True)
    phone_code = models.CharField(max_length=7, unique=True)


    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self) -> str:
        return f"self.name"


class State_Department(CommonModel):

    name = models.CharField(max_length=56, unique=True)
    iso_2 = models.CharField(max_length=2, unique=True)
    iso_3 = models.CharField(max_length=3, unique=True)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "States or Departments"

    def __str__(self) -> str:
        return f"self.name"


class City(CommonModel):

    name = models.CharField(max_length=56, unique=True)
    iso_name_2 = models.CharField(max_length=2, unique=True)
    iso_name_3 = models.CharField(max_length=3, unique=True)
    state_departments = models.ForeignKey(State_Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self) -> str:
        return f"{self.name}"
