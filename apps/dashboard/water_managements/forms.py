from django import forms
from django.contrib.auth import get_user_model
from apps.main.refectories.models import Refectory
from apps.main.water_tanks.models import WaterTank
from apps.main.water_managements.models import WaterManagement

class WaterManagementForm(forms.ModelForm):
    class Meta:
        model = WaterManagement
        fields = [            
                'water_liters',
                'water_amount',
                'operation_description',
                ]

    def clean(self):
        super(WaterManagementForm, self).clean()
        water_liters = self.cleaned_data.get('water_liters')
        water_amount = self.cleaned_data.get('water_amount')

        if water_liters <= 0:
            self._errors['water_liters'] = self.error_class([
                'Volumen menor o igual a 0'])
        elif water_amount < 0:
            self._errors['water_amount'] = self.error_class([
                'Volumen menor a 0'])            
