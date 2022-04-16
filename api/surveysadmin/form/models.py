from django.conf import settings
from django.db import models
from api.surveysadmin.localization.models import Country, StateDepartment
from api.surveysadmin.commons.models import (
    CommonFieldsModel,
    CommonFormsModel,
    CommonOptionTypesModel,
)


# Create your models here.
class FormCategory(CommonOptionTypesModel):
    class Meta:
        db_table = "forms_categories"
        verbose_name_plural = "Forms Categories"

    def __str__(self) -> str:
        return f"{self.name}"


class FormTemplate(CommonFieldsModel):
    form_body = models.JSONField()
    is_draft = models.BooleanField(default=False)
    form_category = models.ForeignKey(FormCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "forms_templates"
        verbose_name_plural = "Forms Templates"

    def __str__(self) -> str:
        return f"{self.name}"


class FormTemplateByCountry(CommonFormsModel):
    form_template = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = "forms_templates_by_country"

    def __str__(self) -> str:
        return f"{self.name}"


class FormTemplateByStateDepartment(CommonFormsModel):
    form_template = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
    state_department = models.ForeignKey(StateDepartment, on_delete=models.CASCADE)

    class Meta:
        db_table = "forms_templates_by_states_departments"

    def __str__(self) -> str:
        return f"{self.name}"


class FilledFormTemplate(CommonFieldsModel):
    filled_form_body = models.JSONField()
    is_draft = models.BooleanField(default=False)
    form_template = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)

    class Meta:
        db_table = "filled_forms_templates"
        verbose_name_plural = "Filled Forms Templates"

    def __str__(self) -> str:
        return f"{self.name}"
