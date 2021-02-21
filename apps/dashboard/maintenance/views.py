from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

#from .forms import RefectoryForm, WaterTankForm, WaterExtraFieldsForm
from apps.main.maintenance.models import Maintenance
from apps.main.refectories.models import Refectory

class RefectoriesMaintenanceListView(ListView):
    template_name = "maintenance/refectories_maintenance_list.html"
    queryset = Refectory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = Refectory.objects.order_by('id')
        
        context['object_list'] = []

        for i in query:
            if len(i.user_asigned.all()) != 0:
                mandated =''
                for j in i.user_asigned.all():
                    mandated = mandated + str(j.name)+' '+str(j.last_name)
                    if j:
                        mandated = mandated + ' - '
            else:
                mandated = '(por asignar)'
            context['object_list'].append({'id':i.id, 'name':i.name, 
            'address':i.address, 'capacity':i.water_tank.capacity,'mandated':mandated })
        return context  