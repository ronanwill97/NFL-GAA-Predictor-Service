import uuid

from django.db import models
from NFL.models.fixture import Fixture


class Response(models.Model):
    phone_number = models.IntegerField(null=False)
    name = models.CharField(max_length=255, null=False)
    form_uuid = models.UUIDField(default=uuid.uuid4(), null=False)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    selection = models.CharField(max_length=255, null=False)

    class Meta:
        app_label = 'NFL'
