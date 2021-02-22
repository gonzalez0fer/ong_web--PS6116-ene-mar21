from django.conf import settings
from django.db import models
from datetime import datetime  
from django.dispatch import receiver
from django.db.models.signals import post_save
from model_utils.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.main.refectories.models import Refectory

class WaterTank(TimeStampedModel):
    
    capacity = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    current_liters = models.IntegerField(
        blank = True,
        null = True,
        validators=[
            MinValueValidator(0),
        ]
    )

    last_fill_date = models.DateTimeField(
        blank=True,
        null = True,        
    )

    description = models.TextField(
        max_length=600,
        blank=True, 
        null=True
        )

    refectory = models.OneToOneField(
        Refectory, 
        blank=True, 
        null=True, 
        related_name='water_tank',
        on_delete = models.SET_NULL,
        ) 

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        )
