from django.db import models


class Refectory(models.Model):
    name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
        )
        
    address = models.TextField(
        max_length=600,
        blank=True, 
        null=True
        )

    capacity = models.IntegerField(
        blank=True, 
        null=True
        )


    def __str__(self):
        return self.name