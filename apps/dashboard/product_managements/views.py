from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from django.http import HttpResponse

from .forms import ProductManagementForm, ProductForm
from apps.main.refectories.models import Refectory
from apps.main.products.models import Product
from apps.main.product_managements.models import ProductManagement


class ProductManagementListView(ListView):
    template_name = "product_managements/product_management_list.html"
    queryset = ProductManagement.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object_list'] = []
        context['refectory_data'] = []

        refectory = Refectory.objects.get(id=self.kwargs['pk'])
        product = Product.objects.filter(refectory=refectory).order_by('created')
        

        for j in product:
            query = ProductManagement.objects.filter(product=j).order_by('created')
            
            for i in query:
                
                context['object_list'].append({
                        'id':i.id,
                        'product_name':i.product.product_name,
                        'operation_type':i.operation_type,
                        'product_quantity':i.product_quantity,
                        'product_unitary_amount':i.product_unitary_amount,
                        'product_total_ammount':i.product_total_amount,
                        'created': i.created,
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


class ProductManagementListSingleView(ListView):
    template_name = "product_managements/product_management_list.html"
    queryset = ProductManagement.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        product = Product.objects.get(id=self.kwargs['pk'])
        query = ProductManagement.objects.filter(product=product).order_by('created')
        
        context['object_list'] = []
        context['refectory_data'] = []

        for i in query:
            
            context['object_list'].append({
                    'id':i.id,
                    'product_name':i.product.product_name,
                        'operation_type':i.operation_type,
                        'product_quantity':i.product_quantity,
                        'product_unitary_amount':i.product_unitary_amount,
                        'product_total_ammount':i.product_total_amount,
                        'created_by':i.created_by.profile.name,
            })

        context['refectory_data'].append({
            'id':product.refectory.id,
            'refectory_name': product.refectory.name,
            'refectory_address': product.refectory.address,
            })
        return context 

class ProductManagementCreateView(CreateView):
    model = ProductManagement
    queryset = ProductManagement.objects.all()
    form_class = ProductManagementForm
    template_name = "product_managements/product_management_create.html"
    success_url = "/dashboard/refectory/"

    def get_context_data(self, **kwargs):

        context = super(ProductManagementCreateView, self).get_context_data(**kwargs)

        if 'product_form' not in context:
            context['product_form'] = ProductForm()
        return context

    def post(self, request, *args, **kwargs):

        self.object = None
        form = self.get_form()

        product_form = ProductForm(request.POST)
        
        if form.is_valid() and product_form.is_valid():
            return self.form_valid(form, product_form)
        else:
            return self.form_invalid(form, product_form)

    def form_valid(self, form, product_form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        
        product_object = product_form.save(commit=False)
        product_object.product_name = self.object.product
        product_object.total_product_quantity = self.object.product_quantity
        #product_object.refectory.id = self.kwargs['pk'] 
        product_object.created_by = self.request.user
        product_object.save()
        return super().form_valid(form)

    def form_invalid(self, form, product_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                product_form=product_form,
            )
        )
