from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.mixins import RetrieveModelMixin

from api.surveysadmin.localization.models import Country, StateDepartment, City
from api.surveysadmin.localization.serializers import (
    CountrySerializer,
    StateDepartmentSerializer,
)


# Create your views here.
class CountryViewSet(ReadOnlyModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all().order_by("-updated_date")
    pagination = PageNumberPagination


class StateDepartmentViewSet(ReadOnlyModelViewSet):
    queryset = StateDepartment.objects.all().order_by("-updated_date")
    serializer_class = StateDepartmentSerializer
    pagination = PageNumberPagination


class CityViewSet(ReadOnlyModelViewSet):
    queryset = StateDepartment.objects.all().order_by("-updated_date")
    serializer_class = City
    pagination = PageNumberPagination
