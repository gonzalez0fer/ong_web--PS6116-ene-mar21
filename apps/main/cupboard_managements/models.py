from django.conf import settings
from django.db import models
from datetime import datetime  
from model_utils.models import TimeStampedModel

from apps.main.cupboards.models import Cupboard


class CupboardManagement(TimeStampedModel):

    class OperationType(models.TextChoices):
        """
        	Every type of issue
        """
        Ingreso     =   'Ingreso'
        Egreso     =   'Egreso'
        NONE        =   'none'


    cupboard =  models.ForeignKey(
        Cupboard, 
        blank=True, 
        null=True, 
        related_name='product',
        on_delete = models.SET_NULL,
        ) 

    operation_type = models.CharField(
        max_length=10, 
        null=False, 
        choices=OperationType.choices, 
        default = OperationType.NONE
    )

    product_quantity = models.IntegerField(
        blank = True,
        null = True,
    )

    product_weight = models.IntegerField(
        blank = True,
        null = True,
    )

    product_amount = models.IntegerField(
        blank = True,
        null = True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'creator_user'
        )