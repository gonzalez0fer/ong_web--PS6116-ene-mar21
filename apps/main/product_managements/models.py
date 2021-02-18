from django.conf import settings
from django.db import models
from datetime import datetime  
from model_utils.models import TimeStampedModel

from apps.main.products.models import Product


class ProductManagement(TimeStampedModel):

    class OperationType(models.TextChoices):
        """
        	Every type of issue
        """
        INGRESO     =   'ingreso'
        CONSUMO     =   'consumo'
        NONE        =   'none'


    product_cod =  models.ForeignKey(
        Product, 
        blank=True, 
        null=True, 
        related_name='product',
        to_field='product_name',
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

    product_unitary_amount = models.IntegerField(
        blank = True,
        null = True,
    )

    product_total_amount = models.IntegerField(
        blank = True,
        null = True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'user_creator'
        )