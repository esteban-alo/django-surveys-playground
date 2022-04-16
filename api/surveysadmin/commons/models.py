from uuid import uuid4
from django.db import models


class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).title()


class CommonFieldsModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid4(), editable=False)

    class Meta:
        abstract = True


class CommonFormsModel(CommonFieldsModel):
    is_enabled = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CommonOptionTypesModel(CommonFieldsModel):
    type_name = models.CharField(max_length=150)

    class Meta:
        abstract = True
