from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

#from .forms import RefectoryForm, WaterTankForm, WaterExtraFieldsForm
from apps.main.water_tanks.models import WaterTank
from apps.main.users.models import CustomUser
from apps.main.water_tanks.models import WaterTank
from apps.main.refectories.models import Refectory
from apps.dashboard.refectories.forms import WaterExtraFieldsForm

@method_decorator([login_required, superuser_required], name='dispatch')
class TanksListView(ListView):
    template_name = "water_tanks/tanks_list.html"
    queryset = WaterTank.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = WaterTank.objects.order_by('id')

        context['object_list'] = []

        for i in query:
            refectory = Refectory.objects.get(id=i.refectory_id)
            context['object_list'].append({
                    'id':i.id, 
                    'capacity':i.capacity, 
                    'current_liters':i.current_liters, 
                    'last_fill_date':i.last_fill_date, 
                    'refectory_name':refectory
            })  
        return context

class WaterTankSingleListView(ListView):
    template_name = "water_tanks/tanks_list_guest.html"
    queryset = WaterTank.objects.all()
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = WaterTank.objects.filter(refectory_id=self.request.user.profile.refectory.id).order_by('id')
        
        context['object_list'] = []

        for i in query:
            
            context['object_list'].append({
                    'id':i.id, 
                    'capacity':i.capacity,
                    'current_liters':i.current_liters,
                    'last_fill_date':i.last_fill_date,
            })  

            context['water_extra_fields'] = WaterExtraFieldsForm(
                initial = {'water_percent':(i.current_liters * 100)//i.capacity,
                })

        return context