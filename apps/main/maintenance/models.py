from django.db import models

from django.conf import settings
from django.db import models
from datetime import datetime  
from django.dispatch import receiver
from django.db.models.signals import post_save
from model_utils.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# fecha, responsable, resultado y observacion. 
# sin embargo, ahora con la nueva
# info  que manejamos hoy habria que 
# indicar a que cosa se le realizo (tanque o planta)

class Maintenance(TimeStampedModel):

    equipment = models.CharField(
        max_length=20,
        null=False
    )

    in_charge = models.TextField(
        max_length=30,
        null=False,
    )

    #lol
    made_date = models.DateTimeField(
        blank=True,
        null=True,
    )

    observation = models.TextField(
        max_length=600,
        blank=True,
        null=True,
    )

    results = models.TextField(
        max_length=600,
        blank=False,
        null=True,
    )
