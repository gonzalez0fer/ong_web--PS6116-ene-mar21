from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

#from .forms import RefectoryForm, WaterTankForm, WaterExtraFieldsForm
from apps.main.maintenance.models import Maintenance

class MaintenanceListView(ListView):
    template_name = "maintenance/maintenance_list.html"
    queryset = Maintenance.objects.all()