from django.conf import settings
from django.db import models
from datetime import datetime  
from model_utils.models import TimeStampedModel

from apps.main.refectories.models import Refectory


class Product(TimeStampedModel):

    product_name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
        )

    total_product_quantity = models.IntegerField(
        blank = True,
        null = True,
    )

    product_unit =  models.CharField(
        max_length=10, 
        blank=True, 
        null=True
    )

    is_spare_part = models.BooleanField(
        default=False
    )    

    refectory = models.ForeignKey(
        Refectory, 
        blank=True, 
        null=True, 
        related_name='product',
        on_delete = models.SET_NULL,
        ) 

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        )