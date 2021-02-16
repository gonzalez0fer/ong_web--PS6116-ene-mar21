from django.conf import settings
from django.db import models
from datetime import datetime  
from model_utils.models import TimeStampedModel

from apps.main.water_tanks.models import WaterTank


class WaterManagement(TimeStampedModel):

    class OperationType(models.TextChoices):
        """
        	Every type of issue
        """
        INGRESO     =   'ingreso'
        CONSUMO     =   'consumo'
        NONE        =   'none'


    cupboard =  models.ForeignKey(
        WaterTank, 
        blank=True, 
        null=True, 
        related_name='water',
        on_delete = models.SET_NULL,
        ) 

    operation_type = models.CharField(
        max_length=10, 
        null=False, 
        choices=OperationType.choices, 
        default = OperationType.NONE
    )

    water_liters = models.IntegerField(
        blank = True,
        null = True,
    )

    water_amount = models.IntegerField(
        blank = True,
        null = True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        )