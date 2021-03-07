from django.conf import settings
from django.db import models
from datetime import datetime  
from model_utils.models import TimeStampedModel

from apps.main.equipments.models import Equipment
from apps.main.products.models import Product
from apps.main.product_managements.models import ProductManagement

class Maintenance(TimeStampedModel):
    #foreign key
    equipment = models.CharField(
        max_length=20,
        null=False
    )

    activity = models.TextField(
        max_length=600,
        blank=True,
        null=True,
    )

    comments = models.TextField(
        max_length=600,
        blank=False,
        null=True,
    )

    product =  models.ForeignKey(
        Product, 
        blank=True, 
        null=True, 
        related_name='product_consumed',
        on_delete = models.SET_NULL,
    )

    product_quantity = models.IntegerField(
        blank = True,
        null = True,
    )

    product_operation =  models.ForeignKey(
        ProductManagement, 
        blank=True, 
        null=True, 
        related_name='product_operation',
        on_delete = models.SET_NULL,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'user_operator'
    )
