import uuid
from django.db import models
from .settings import PULSE_TYPE_CHOICES

# Create your models here.


class Pulse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=PULSE_TYPE_CHOICES)
    max_rabi_rate = models.FloatField()
    polar_angle = models.FloatField()
