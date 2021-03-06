from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db.models.deletion import SET_NULL
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from model_utils.models import TimeStampedModel

from .managers import CustomUserManager

from apps.main.refectories.models import Refectory

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), 
    unique=True
    )

    is_staff = models.BooleanField(
        default=False
        )

    is_active = models.BooleanField(
        default=True
        )

    date_joined = models.DateTimeField(
        default=timezone.now
        )
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(TimeStampedModel):
    name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
        )

    last_name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
        )

    address = models.TextField(
        max_length=600,
        blank=True, 
        null=True
        )

    about = models.TextField(
        max_length=1000,
        blank=True, 
        null=True
        )

    user = models.OneToOneField(
        CustomUser, 
        null=True, 
        on_delete=models.SET_NULL, 
        related_name = 'profile'
        )
    
    refectory = models.ForeignKey(
        Refectory, 
        blank=True, 
        null=True, 
        related_name='user_asigned',
        on_delete = models.SET_NULL,
        )

    def __str__(self):
        return self.name +' ' + self.last_name

    @receiver(post_save, sender=CustomUser) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
