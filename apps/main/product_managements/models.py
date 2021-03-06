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
        Ingreso     =   'Ingreso'
        Egreso     =   'Egreso'

    class OperationUnit(models.TextChoices):
        """
        	Every type of issue
        """
        KILOGRAMO = 'Kg',
        GRAMO = 'g',
        LITROS = 'L',
        MILILITROS = 'ml',
        UNIDADES = 'Unidad(es)',
        PIEZAS = 'Pieza(s)'


    product_cod =  models.ForeignKey(
        Product, 
        blank=True, 
        null=True, 
        related_name='product',
        on_delete = models.SET_NULL,
        )

    product_name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
    )

    product_unit =  models.CharField(
        max_length=10, 
        null=False, 
        choices=OperationUnit.choices, 
        default = OperationUnit.UNIDADES
    )

    operation_type = models.CharField(
        max_length=10, 
        null=False, 
        choices=OperationType.choices, 
        default = OperationType.Ingreso
    )

    product_quantity = models.IntegerField(
        blank = True,
        null = True,
    )

    product_unitary_amount = models.FloatField(
        blank = True,
        null = True,
    )

    product_total_amount = models.FloatField(
        blank = True,
        null = True,
    )

    is_spare_part = models.BooleanField(
        default=False
    )

    is_maintenance = models.BooleanField(
        default=False
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'user_creator'
        )