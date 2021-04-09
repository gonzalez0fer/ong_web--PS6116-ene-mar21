# Create your models here.
from django.conf import settings
from django.db import models
from datetime import datetime  
from model_utils.models import TimeStampedModel

from apps.main.refectories.models import Refectory


class Notifications(TimeStampedModel):

    class NotificationType(models.TextChoices):
        """
        	Every type of issue
        """
        AGUA     =   'Agua'
        SUMINISTROS     =   'Suministros'
        ALIMENTOS = 'Alimentos'
        MANTENIMIENTO = 'Mantenimiento'
        NONE = ''

    class NotificationStatus(models.TextChoices):
        """
        	Every type of issue
        """
        PENDIENTE     =   'Pendiente'
        SOLUCIONADO     =   'Solucionado'

    refectory = models.ForeignKey(
        Refectory, 
        blank=True, 
        null=True, 
        related_name='refectory_notification',
        on_delete = models.SET_NULL,
    ) 

    read = models.BooleanField(
        default=False
    )

    notification_type = models.CharField(
        max_length=20, 
        null=False, 
        choices=NotificationType.choices, 
        default = NotificationType.NONE
    )

    notification_message = models.CharField(
        max_length=100,
        null=False
    )


    notification_status = models.CharField(
        max_length=20, 
        null=False, 
        choices=NotificationStatus.choices, 
        default = NotificationStatus.PENDIENTE
    )

    user_notification = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
    )
