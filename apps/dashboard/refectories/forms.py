from django import forms
from django.contrib.auth import get_user_model
from apps.main.refectories.models import Refectory
from apps.main.water_tanks.models import WaterTank


class RefectoryForm(forms.ModelForm):
    class Meta:
        model = Refectory
        fields = [            
                'name',
                'address',
                'capacity',
                'description',
                ]
        
class WaterTankForm(forms.ModelForm):
    class Meta:
        model = WaterTank
        fields = [            
                'capacity',
                'current_liters',
                ]
        