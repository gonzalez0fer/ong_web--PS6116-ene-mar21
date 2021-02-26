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

    class OperationDescription(models.TextChoices):
        """
        	Every type of issue
        """
        CISTERNA     =   'Cisterna'
        TUBERIA     =   'Tuberia'
        MANTENIMIENTO = 'Mantenimiento'
        VENTA = 'Venta'
        USO_INTERNO = 'Uso Interno'



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
        default = OperationType.INGRESO
    )

    water_liters = models.IntegerField(
        blank = True,
        null = True,
    )

    water_amount = models.FloatField(
        blank = True,
        null = True,
    )

    water_price_total = models.FloatField(
        blank = True,
        null = True,
    )

    operation_description = models.CharField(
        max_length=20, 
        null=False, 
        choices=OperationDescription.choices, 
        default = OperationDescription.VENTA
    )    

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        )