from django import forms
from django.contrib.auth import get_user_model

from apps.main.suppliers.models import Supplier


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'company_name',
            'company_contact_name',
            'company_rif',
            'company_address',
            'company_phone',
            'company_description',
            ]