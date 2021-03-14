from django.conf import settings
from django.db import models
from datetime import datetime  
from model_utils.models import TimeStampedModel

from apps.main.refectories.models import Refectory
from apps.main.products.models import Product

class Equipment(TimeStampedModel):

    class Periods(models.TextChoices):
        """
        	Every type of issue
        """
        SEMANAL = 'Semanal',
        QUINCENAL = 'Quincenal',
        MENSUAL = 'Mensual',
        TRIMESTRAL = 'Trimestral',
        SEMESTRAL = 'Semestral',
        ANUAL = 'Anual'
        BIENAL = 'Bienal'
        TRIENAL = 'Trienal'


    name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
    )

    brand = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
    )

    equipment_model = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
    )

    power = models.FloatField(
        blank = True,
        null = True,
    )

    inlet_diameter = models.FloatField(
        blank = True,
        null = True,
    )

    diameter = models.FloatField(
        blank = True,
        null = True,
    )

    height = models.FloatField(
        blank = True,
        null = True,
    )

    volume = models.FloatField(
        blank = True,
        null = True,
    )

    measurements = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
    )

    spare_part = models.ForeignKey(
        Product, 
        blank=True, 
        null=True, 
        related_name='spare_equipment',
        on_delete = models.SET_NULL,
    )
    
    flow = models.FloatField(
        blank = True,
        null = True,
    )

    light_bulb_size = models.FloatField(
        blank = True,
        null = True,
    )

    quartz_size = models.FloatField(
        blank = True,
        null = True,
    )

    maintenance_frequency = models.CharField(
        max_length=20, 
        null=False, 
        choices=Periods.choices, 
        default = Periods.SEMANAL
    )

    instructions = models.TextField(
        max_length=2000,
        blank=True,
        null=True,
    )

    refectory = models.ForeignKey(
        Refectory, 
        blank=True, 
        null=True, 
        related_name='equipment',
        on_delete = models.SET_NULL,
        ) 

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        )