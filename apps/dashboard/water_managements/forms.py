from django import forms
from django.contrib.auth import get_user_model
from apps.main.refectories.models import Refectory
from apps.main.water_tanks.models import WaterTank
from apps.main.water_managements.models import WaterManagement

class WaterManagementForm(forms.ModelForm):
    class Meta:
        model = WaterManagement
        fields = [            
                'operation_type',
                'water_liters',
                'water_amount',
                ]