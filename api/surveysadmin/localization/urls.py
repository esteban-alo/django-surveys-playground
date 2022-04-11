from rest_framework import routers

from api.surveysadmin.localization.views import CountryViewSet

countries_router = routers.DefaultRouter()
countries_router.register("localization", viewset=CountryViewSet, basename="localization")
