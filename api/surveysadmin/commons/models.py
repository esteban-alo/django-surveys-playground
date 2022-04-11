from uuid import uuid4
from django.db import models


class CommonModel(models.Model):

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid4(), editable=False)

    class Meta:
        abstract = True
