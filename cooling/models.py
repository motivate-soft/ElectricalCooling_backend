from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import JSONField
from accounts.models import CustomUser


class Cooling(models.Model):
    class Meta:
        db_table = 'cooling_model'
    components = ArrayField(JSONField(null=True, blank=True), blank=True, null=True)
    losses = ArrayField(JSONField(null=True, blank=True), blank=True, null=True)
    faces = ArrayField(JSONField(null=True, blank=True), blank=True, null=True)
    passages = ArrayField(JSONField(null=True, blank=True), blank=True, null=True)
    fluids = ArrayField(JSONField(null=True, blank=True), blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='cooling_model', null=True)
