from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

from apps.main.refectories.models import Refectory
from apps.main.cupboards.models import Cupboard

@method_decorator([login_required, superuser_required], name='dispatch')
class RefectoriesCupboardListView(ListView):
    template_name = "cupboards/refectories_cupboard_list.html"
    queryset = Refectory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = Refectory.objects.order_by('id')
        
        context['object_list'] = []

        for i in query:
            mandated = []
            if len(i.user_asigned.all()) > 0:
                for j in i.user_asigned.all():
                    if j.name and j.last_name:
                        mandated.append (str(j.name)+' '+str(j.last_name)+' - '+'('+str(j.user.email)+')')
                    else:
                        mandated.append('(nombre sin asignar) - '+'('+str(j.user.email)+')')
            else:
                mandated.append('(por asignar)')
                            
            context['object_list'].append({'id':i.id, 'name':i.name, 
            'address':i.address, 'capacity':i.water_tank.capacity,'mandated':mandated })
        return context

@method_decorator([login_required, superuser_required], name='dispatch')
class CupboardsListView(ListView):
    template_name = "cupboards/cupboard_list.html"
    queryset = Cupboard.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        refectory = Refectory.objects.get(id=self.kwargs['pk'])
        query = Cupboard.objects.filter(refectory=refectory).order_by('id')
        
        context['object_list'] = []
        context['refectory_data'] = []

        for i in query:
            
            context['object_list'].append({
                    'id':i.id, 
                    'product_name':i.product_name,
                    'total_product_quantity':i.total_product_quantity,
            })

        context['refectory_data'].append({
            'id':refectory.id,
            'refectory_name': refectory.name,
            'refectory_address': refectory.address,
            })
        return context 

class CupboardsSingleListView(ListView):
    template_name = "cupboards/cupboard_list.html"
    queryset = Cupboard.objects.all()

    def get_object(self):
        return Refectory.objects.get(pk=self.request.user.profile.refectory.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        refectory = Refectory.objects.get(id=self.request.user.profile.refectory.id)
        query = Cupboard.objects.filter(refectory=refectory).order_by('id')
        
        context['object_list'] = []
        context['refectory_data'] = []

        for i in query:
            
            context['object_list'].append({
                    'id':i.id, 
                    'product_name':i.product_name,
                    'total_product_quantity':i.total_product_quantity,
            })

        context['refectory_data'].append({
            'id':refectory.id,
            'refectory_name': refectory.name,
            'refectory_address': refectory.address,
            })
        return context 