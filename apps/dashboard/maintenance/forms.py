from django.forms import ModelForm
from apps.main.maintenance.models  import Maintenance


class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = ['activity', 'comments', 'product_quantity']