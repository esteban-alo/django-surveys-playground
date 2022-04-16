from rest_framework import routers

from api.surveysadmin.localization.views import (
    CountryViewSet,
    StateDepartmentViewSet,
    CityViewSet,
)

localization_router = routers.DefaultRouter()
localization_router.register(
    "localization/country",
    viewset=CountryViewSet,
    basename="country",
)

localization_router.register(
    "localization/state_department",
    viewset=StateDepartmentViewSet,
    basename="state",
)

localization_router.register(
    "localization/city",
    viewset=CityViewSet,
    basename="city",
)
