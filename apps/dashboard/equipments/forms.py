from django import forms
from django.contrib.auth import get_user_model

from apps.main.equipments.models import Equipment


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = [
            'name',
            'brand',
            'equipment_model',
            'power',
            'inlet_diameter',
            'diameter',
            'height',
            'volume',
            'measurements',
            'flow',
            'light_bulb_size',
            'quartz_size',
            'maintenance_frequency',
            'spare_part',
            'instructions',
            ]