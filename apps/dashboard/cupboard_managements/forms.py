from django.forms import ModelForm
from apps.main.cupboard_managements.models  import CupboardManagement

class CupboardManagementForm(ModelForm):
    class Meta:
        model = CupboardManagement
        fields = ['product_name', 'operation_type','product_quantity','product_unitary_amount']