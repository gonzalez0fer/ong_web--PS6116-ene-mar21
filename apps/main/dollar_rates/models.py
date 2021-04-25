from django.db import models
from datetime import datetime  
from model_utils.models import TimeStampedModel

class DollarRate(TimeStampedModel):

    value = models.FloatField(
        blank = True,
        null = True,
    )