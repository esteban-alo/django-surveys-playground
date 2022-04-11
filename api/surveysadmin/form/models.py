from uuid import uuid4
from django.db import models
from api.surveysadmin.localization.models import Country, State_Department
from api.surveysadmin.commons.models import CommonModel


# Create your models here.
class Form(CommonModel):
    form_body = models.JSONField()
    uuid = models.UUIDField(default=uuid4(), editable=False)
