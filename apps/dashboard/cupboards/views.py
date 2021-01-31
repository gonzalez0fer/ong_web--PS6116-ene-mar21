from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import HttpResponse

from apps.main.refectories.models import Refectory
from apps.main.cupboards.models import Cupboard



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
                    'total_product_weight':i.total_product_weight,
                    'total_product_quantity':i.total_product_quantity,
                    'total_product_investment':i.total_product_investment,
            })

        context['refectory_data'].append({
            'id':refectory.id,
            'refectory_name': refectory.name,
            'refectory_address': refectory.address,
            })
        return context 