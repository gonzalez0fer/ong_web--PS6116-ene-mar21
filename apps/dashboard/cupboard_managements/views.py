from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import HttpResponse

from apps.main.refectories.models import Refectory
from apps.main.cupboards.models import Cupboard
from apps.main.cupboard_managements.models import CupboardManagement


class CupboardManagementListView(ListView):
    template_name = "cupboard_managements/cupboard_management_list.html"
    queryset = CupboardManagement.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object_list'] = []
        context['refectory_data'] = []

        refectory = Refectory.objects.get(id=self.kwargs['pk'])
        cupboard = Cupboard.objects.filter(refectory=refectory).order_by('created')
        

        for j in cupboard:
            query = CupboardManagement.objects.filter(cupboard=j).order_by('created')
            
            for i in query:
                
                context['object_list'].append({
                        'id':i.id,
                        'product_name':i.cupboard.product_name,
                        'operation_type':i.operation_type,
                        'product_quantity':i.product_quantity,
                        'product_weight':i.product_weight,
                        'product_amount':i.product_amount,
                        'created':i.created,
                        'created_by':i.created_by.profile.name,
                })
        try:
            context['refectory_data'].append({
                'id':refectory.id,
                'refectory_name': refectory.name,
                'refectory_address': refectory.address,
                })
        except:
            pass
        return context 


class CupboardManagementListSingleView(ListView):
    template_name = "cupboard_managements/cupboard_management_list.html"
    queryset = CupboardManagement.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        cupboard = Cupboard.objects.get(id=self.kwargs['pk'])
        query = CupboardManagement.objects.filter(cupboard=cupboard).order_by('created')
        
        context['object_list'] = []
        context['refectory_data'] = []

        for i in query:
            
            context['object_list'].append({
                    'id':i.id,
                    'product_name':i.cupboard.product_name,
                    'operation_type':i.operation_type,
                    'product_quantity':i.product_quantity,
                    'product_weight':i.product_weight,
                    'product_amount':i.product_amount,
                    'created':i.created,
                    'created_by':i.created_by.profile.name,
            })

        context['refectory_data'].append({
            'id':cupboard.refectory.id,
            'refectory_name': cupboard.refectory.name,
            'refectory_address': cupboard.refectory.address,
            })
        return context 