from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,TemplateView
from django.http import HttpResponse, HttpResponseRedirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

from .forms import CupboardManagementForm
from apps.main.refectories.models import Refectory
from apps.main.cupboards.models import Cupboard
from apps.main.cupboard_managements.models import CupboardManagement

@method_decorator([login_required, superuser_required], name='dispatch')
class CupboardManagementListView(ListView):
    template_name = "cupboard_managements/cupboard_management_list.html"
    queryset = CupboardManagement.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object_list'] = []
        context['refectory_data'] = []

        refectory = Refectory.objects.get(id=self.kwargs['refectory_id'])
        cupboard = Cupboard.objects.filter(refectory=refectory).order_by('created')
        

        for j in cupboard:
            query = CupboardManagement.objects.filter(cupboard=j).order_by('created')
            
            for i in query:
                
                context['object_list'].append({
                        'id':i.id,
                        'product_name':i.product_name,
                        'operation_type':i.operation_type,
                        'product_quantity':i.product_quantity,
                        'product_unitary_amount':i.product_unitary_amount,
                        'product_total_amount':i.product_total_amount,
                        'created':i.created,
                        'created_by':str(i.created_by.profile.name)+' '+str(i.created_by.profile.last_name),
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
        
        refectory = Refectory.objects.get(id=self.request.user.profile.refectory.id)
        cupboard = Cupboard.objects.filter(refectory_id=refectory.id).order_by('created')
        
        context['object_list'] = []
        context['refectory_data'] = []
        
        for j in cupboard:
            query = CupboardManagement.objects.filter(cupboard=j).order_by('created')
            
            for i in query:
                
                context['object_list'].append({
                        'id':i.id,
                        'product_name':i.product_name,
                        'operation_type':i.operation_type,
                        'product_quantity':i.product_quantity,
                        'product_unitary_amount':i.product_unitary_amount,
                        'product_total_amount':i.product_total_amount,
                        'created':i.created,
                        'created_by':str(i.created_by.profile.name)+' '+str(i.created_by.profile.last_name),
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

@method_decorator([login_required, superuser_required], name='dispatch')
class CupboardManagementCreateView(CreateView):
    model = CupboardManagement
    queryset = CupboardManagement.objects.all()
    form_class = CupboardManagementForm
    template_name = "cupboard_managements/cupboard_management_create.html"

    def get_success_url(self):
        if self.request.user.is_superuser:
            success_url = reverse('dashboard:cupboard_managements:list_cupboard_management',kwargs={'refectory_id':self.kwargs['refectory_id']}) 
        else:
            pass  
        return success_url

    def get_context_data(self, **kwargs):
        context = super(CupboardManagementCreateView, self).get_context_data(**kwargs)
        query = Cupboard.objects.filter(refectory_id=self.kwargs['refectory_id']).order_by('product_name')

        context['product_info'] = []
        context['product_operation'] = self.kwargs['op_type']
        for i in query:
            context['product_info'].append({
                "product_name": i.product_name,
                "product_quantity": i.total_product_quantity,
            })

        context['refectory'] = {
            'id' : self.kwargs['refectory_id'],
        }
        return context 

    def post(self, request, *args, **kwargs):

        self.object = None
        form = self.get_form()
        product, created = Cupboard.objects.get_or_create(product_name=form.data['product_name'],refectory_id=self.kwargs['refectory_id'])

        if form.is_valid():
            return self.form_valid(form, product, created)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, product, created):
        self.object = form.save(commit=False)
        self.object.cupboard = product
        self.object.product_total_amount = self.object.product_quantity * self.object.product_unitary_amount
        #si no existia el producto, se creo en el get or create
        if created:
            product.total_product_quantity = self.object.product_quantity
            product.created_by = self.request.user
            product.refectory_id = self.kwargs['refectory_id']
        #ya existia el producto
        else:
            if self.object.operation_type == 'Ingreso':    
                product.total_product_quantity = product.total_product_quantity + self.object.product_quantity
                product.created_by = self.request.user
                product.refectory_id = self.kwargs['refectory_id']                    
            else:
                #si intento sacar mas de lo que hay
                if self.object.product_quantity > product.total_product_quantity:
                    return self.form_invalid(form)
                product.total_product_quantity = product.total_product_quantity - self.object.product_quantity
                product.created_by = self.request.user
                product.refectory_id = self.kwargs['refectory_id']                

        product.save()
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class CupboardManagementCreateViewGuest(CreateView):
    model = CupboardManagement
    queryset = CupboardManagement.objects.all()
    form_class = CupboardManagementForm
    template_name = "cupboard_managements/cupboard_management_create.html"
    success_url = "/dashboard/cupboard-management/operations"

    def get_context_data(self, **kwargs):
        context = super(CupboardManagementCreateViewGuest, self).get_context_data(**kwargs)
        query = Cupboard.objects.filter(refectory_id=self.request.user.profile.refectory.id).order_by('product_name')

        context['product_info'] = []
        context['product_operation'] = self.kwargs['op_type']
        for i in query:
            context['product_info'].append({
                "product_name": i.product_name,
                "product_quantity": i.total_product_quantity,
            })

        context['refectory'] = {
            'id' : self.request.user.profile.refectory.id,
        }
        return context 

    def post(self, request, *args, **kwargs):

        self.object = None
        form = self.get_form()
        product, created = Cupboard.objects.get_or_create(product_name=form.data['product_name'],refectory_id=self.request.user.profile.refectory.id)

        if form.is_valid():
            return self.form_valid(form, product, created)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, product, created):
        self.object = form.save(commit=False)
        self.object.cupboard = product
        self.object.product_total_amount = self.object.product_quantity * self.object.product_unitary_amount
        #si no existia el producto, se creo en el get or create
        if created:
            product.total_product_quantity = self.object.product_quantity
            product.created_by = self.request.user
            product.refectory_id = self.request.user.profile.refectory.id
        #ya existia el producto
        else:
            if self.object.operation_type == 'Ingreso':    
                product.total_product_quantity = product.total_product_quantity + self.object.product_quantity
                product.created_by = self.request.user
                product.refectory_id = self.request.user.profile.refectory.id                  
            else:
                #si intento sacar mas de lo que hay
                if self.object.product_quantity > product.total_product_quantity:
                    return self.form_invalid(form)
                product.total_product_quantity = product.total_product_quantity - self.object.product_quantity
                product.created_by = self.request.user
                product.refectory_id = self.request.user.profile.refectory.id                

        product.save()
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

@method_decorator([login_required, superuser_required], name='dispatch')
class CupboardManagementUpdateView(UpdateView):
    form_class = CupboardManagementForm
    model = CupboardManagement 
    queryset = CupboardManagement.objects.all()
    template_name = "cupboard_managements/cupboard_management_update.html"

    def get_success_url(self):
        if self.request.user.is_superuser:
            success_url = reverse('dashboard:cupboard_managements:list_cupboard_management',kwargs={'refectory_id':self.kwargs['refectory_id']})
        else:
            pass  
        return success_url
    
    def get_context_data(self, **kwargs):

        context = super(CupboardManagementUpdateView, self).get_context_data(**kwargs)
        product_info = Cupboard.objects.filter(refectory_id=self.kwargs['refectory_id']).order_by('product_name')
        product_operation = CupboardManagement.objects.filter(cupboard_id=context['object'].cupboard.id)

        context['product_code_operation'] = len(product_operation)
        context['product_info'] = []
        for i in product_info:
            context['product_info'].append({
                'product_name': i.product_name,
                "product_quantity": i.total_product_quantity,
            })

        context['refectory_info'] = {
            'refectory_id':self.kwargs['refectory_id'],
        } 
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        temp = self.object.product_quantity #valor actual
        temp_operation = self.object.operation_type
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form, temp, temp_operation)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, temp, temp_operation):
        self.object = form.save(commit=False)
        self.object.product_total_amount = self.object.product_unitary_amount * self.object.product_quantity
        product = Cupboard.objects.get(product_name=self.object.product_name,refectory_id=self.kwargs['refectory_id'])
        self.object.cupboard = product
        
        #validaciones
        # si no se cambia el tipo de operacion
        if temp_operation == self.object.operation_type:
            if self.object.operation_type == 'Ingreso':
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # restar litros ingresados antiguos     
                product.total_product_quantity = (product.total_product_quantity - temp) + self.object.product_quantity
            else:
                # sumar litros egresados antiguos                
                product.total_product_quantity = (product.total_product_quantity + temp) - self.object.product_quantity
        #si cambia el tipo de operacion en la edicion
        else:
            if self.object.operation_type == 'Ingreso':
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # operacion inversa     
                product.total_product_quantity = (product.total_product_quantity + temp) + self.object.product_quantity
            else:
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # operacion inversa                
                product.total_product_quantity = (product.total_product_quantity - temp) - self.object.product_quantity                     
        product.save()
        return super().form_valid(form)



    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class CupboardManagementUpdateViewGuest(UpdateView):
    form_class = CupboardManagementForm
    model = CupboardManagement 
    queryset = CupboardManagement.objects.all()
    template_name = "cupboard_managements/cupboard_management_update.html"
    success_url = "/dashboard/cupboard-managements/operations"
    
    def get_context_data(self, **kwargs):

        context = super(CupboardManagementUpdateViewGuest, self).get_context_data(**kwargs)
        product_info = Cupboard.objects.filter(refectory_id=self.request.user.profile.refectory.id).order_by('product_name')
        product_operation = CupboardManagement.objects.filter(cupboard_id=context['object'].cupboard.id)

        context['product_code_operation'] = len(product_operation)
        context['product_info'] = []
        for i in product_info:
            context['product_info'].append({
                'product_name': i.product_name,
                "product_quantity": i.total_product_quantity,
            })

        context['refectory_info'] = {
            'refectory_id':self.request.user.profile.refectory.id,
        } 
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        temp = self.object.product_quantity #valor actual
        temp_operation = self.object.operation_type
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form, temp, temp_operation)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, temp, temp_operation):
        self.object = form.save(commit=False)
        self.object.product_total_amount = self.object.product_unitary_amount * self.object.product_quantity
        product = Cupboard.objects.get(product_name=self.object.product_name,refectory_id=self.request.user.profile.refectory.id)
        self.object.cupboard = product
        
        #validaciones
        # si no se cambia el tipo de operacion
        if temp_operation == self.object.operation_type:
            if self.object.operation_type == 'Ingreso':
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # restar litros ingresados antiguos     
                product.total_product_quantity = (product.total_product_quantity - temp) + self.object.product_quantity
            else:
                # sumar litros egresados antiguos                
                product.total_product_quantity = (product.total_product_quantity + temp) - self.object.product_quantity
        #si cambia el tipo de operacion en la edicion
        else:
            if self.object.operation_type == 'Ingreso':
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # operacion inversa     
                product.total_product_quantity = (product.total_product_quantity + temp) + self.object.product_quantity
            else:
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # operacion inversa                
                product.total_product_quantity = (product.total_product_quantity - temp) - self.object.product_quantity                       
        product.save()
        return super().form_valid(form)



    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class ModalTemplate(TemplateView):
    template_name = "cupboard_managements/cupboard_management_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = CupboardManagement.objects.get(pk=self.kwargs['pk'])
        product = Cupboard.objects.get(pk=query.cupboard.id)
        
        context['operation'] = {
            'id':query.id,
            'type':query.operation_type,
            'product_name':query.product_name,
            'product_quantity':query.product_quantity,
            'created':query.created,
            'product_total_quantity':product.total_product_quantity,
            'refectory_id':self.kwargs['refectory_id'],
        }
        return context

def DeleteCupboardManagementOperation(request, refectory_id, pk):
    product_op = get_object_or_404(CupboardManagement, id = pk)
    product = Cupboard.objects.get(pk=product_op.cupboard.id)
    
    if product_op.operation_type == 'Ingreso':
        if product.total_product_quantity - product_op.product_quantity < 0:
            #TODO mensaje de error
            return HttpResponseRedirect("/dashboard/cupboard-management/"+str(refectory_id))
        product.total_product_quantity -= product_op.product_quantity

    else:
        product.total_product_quantity += product_op.product_quantity

    product.save()
    if product.total_product_quantity == 0:
        product.delete()
    
    product_op.delete()
    return HttpResponseRedirect("/dashboard/cupboard-management/"+str(refectory_id))
