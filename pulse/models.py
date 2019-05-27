import uuid
from datetime import datetime
from django.db import models

# Create your models here.


class Pulse(models.Model):

    # choices
    PRIMITIVE = "Primitive"
    CORPSE = "CORPSE"
    GAUSSIAN = "Gaussian"
    CINBB = "CinBB"
    CINSK = "CinSK"
    PULSE_TYPE_CHOICES = (
        (PRIMITIVE, "Primitive"),
        (CORPSE, "CORPSE"),
        (GAUSSIAN, "Gaussian"),
        (CINBB, "CinBB"),
        (CINSK, "CinSK"),
    )

    # database fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=PULSE_TYPE_CHOICES)
    max_rabi_rate = models.FloatField()
    polar_angle = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "pulse"
        verbose_name_plural = "pulses"

    def __str__(self):
        return "%s - %s" % (self.name, self.type)
