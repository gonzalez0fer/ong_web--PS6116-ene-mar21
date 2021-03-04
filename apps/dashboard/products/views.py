from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

from apps.main.refectories.models import Refectory
from apps.main.products.models import Product


@method_decorator([login_required, superuser_required], name='dispatch')
class ProductsListView(ListView):
    template_name = "products/product_list.html"
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        refectory = Refectory.objects.get(id=self.kwargs['pk'])
        query = Product.objects.filter(refectory=refectory).order_by('id')
        
        context['object_list'] = []
        context['refectory_data'] = []

        for i in query:
            
            context['object_list'].append({
                    'id':i.id, 
                    'product_name':i.product_name,
                    'total_product_quantity':i.total_product_quantity,
                    'product_unit':i.product_unit,
            })

        context['refectory_data'].append({
            'id':refectory.id,
            'refectory_name': refectory.name,
            'refectory_address': refectory.address,
            })
        return context 



class ProductsSingleListView(ListView):
    template_name = "products/product_list.html"
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        refectory = Refectory.objects.get(id=self.request.user.profile.refectory.id)
        query = Product.objects.filter(refectory=refectory).order_by('id')
        
        context['object_list'] = []
        context['refectory_data'] = []

        for i in query:
            
            context['object_list'].append({
                    'id':i.id, 
                    'product_name':i.product_name,
                    'total_product_quantity':i.total_product_quantity,
                    'product_unit':i.product_unit,
            })

        context['refectory_data'].append({
            'id':refectory.id,
            'refectory_name': refectory.name,
            'refectory_address': refectory.address,
            })
        return context 