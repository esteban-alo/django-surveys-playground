from rest_framework import serializers
from api.surveysadmin.localization.models import Country, StateDepartment


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


class StateDepartmentSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = StateDepartment
        fields = [
            "name",
            "iso_2",
            "iso_3",
            "country",
            "created_date",
            "updated_date",
            "uuid",
        ]
