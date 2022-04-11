from rest_framework import serializers
from api.surveysadmin.localization.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            "name",
            "iso_name_2",
            "iso_name_3",
            "phone_code",
            "created_date",
            "updated_date",
            "uuid",
        ]
