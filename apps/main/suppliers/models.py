from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel

class Supplier(TimeStampedModel):
    company_name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
        )

    company_contact_name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
        )

    company_rif = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
        )
        
    company_address = models.TextField(
        max_length=600,
        blank=True, 
        null=True
        )

    company_phone = models.IntegerField(
        blank=True, 
        null=True
        )

    company_description = models.TextField(
        max_length=600,
        blank=True, 
        null=True
        )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        )

    def __str__(self):
        return self.company_name