from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,TemplateView
from django.http import HttpResponse
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

from .forms import ProductManagementForm
from apps.main.refectories.models import Refectory
from apps.main.products.models import Product
from apps.main.product_managements.models import ProductManagement

@method_decorator([login_required, superuser_required], name='dispatch')
class ProductManagementListView(ListView):
    template_name = "product_managements/product_management_list.html"
    queryset = ProductManagement.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object_list'] = []
        context['refectory_data'] = []   

        refectory = Refectory.objects.get(id=self.kwargs['refectory_id'])
        product = Product.objects.filter(refectory=refectory.id).order_by('created')
        

        for j in product:
            query = ProductManagement.objects.filter(product_cod=j).order_by('created')
            for i in query:
                context['object_list'].append({
                        'id':i.id,
                        'product_name':j.product_name,
                        'operation_type':i.operation_type,
                        'product_quantity':i.product_quantity,
                        'product_unitary_amount':i.product_unitary_amount,
                        'product_total_amount':i.product_total_amount,
                        'product_unit':i.product_unit,
                        'created': i.created,
                        'created_by':str(i.created_by.profile.name) + ' ' + str(i.created_by.profile.last_name),
                        'product_id': j.id,
                        'is_maintenance': i.is_maintenance,
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

class ProductManagementListViewGuest(ListView):
    template_name = "product_managements/product_management_list.html"
    queryset = ProductManagement.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object_list'] = []
        context['refectory_data'] = []   

        refectory = Refectory.objects.get(id=self.request.user.profile.refectory.id)
        product = Product.objects.filter(refectory=refectory.id).order_by('created')
        

        for j in product:
            query = ProductManagement.objects.filter(product_cod=j).order_by('created')
            for i in query:
                context['object_list'].append({
                        'id':i.id,
                        'product_name':j.product_name,
                        'operation_type':i.operation_type,
                        'product_quantity':i.product_quantity,
                        'product_unitary_amount':i.product_unitary_amount,
                        'product_total_amount':i.product_total_amount,
                        'product_unit':i.product_unit,
                        'created': i.created,
                        'created_by':str(i.created_by.profile.name) + ' ' + str(i.created_by.profile.last_name),
                        'product_id': j.id,
                        'is_maintenance': i.is_maintenance,
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
class ProductManagementCreateView(CreateView):
    model = ProductManagement
    queryset = ProductManagement.objects.all()
    form_class = ProductManagementForm
    template_name = "product_managements/product_management_create.html"

    def get_success_url(self):
        success_url = reverse('dashboard:product_managements:list_product_management',kwargs={'refectory_id':self.kwargs['refectory_id']})    
        return success_url

    def get_context_data(self, **kwargs):
        context = super(ProductManagementCreateView, self).get_context_data(**kwargs)
        query = Product.objects.filter(refectory_id=self.kwargs['refectory_id']).order_by('product_name')

        context['product_info'] = []
        context['product_operation'] = self.kwargs['op_type']
        for i in query:
            context['product_info'].append({
                "product_name": i.product_name,
                "product_quantity": i.total_product_quantity,
                "product_unit": i.product_unit,
            })

        context['refectory'] = {
            'id' : self.kwargs['refectory_id'],
        }
        return context 

    def post(self, request, *args, **kwargs):

        self.object = None
        form = self.get_form()
        product_name_upper = form.data['product_cod'].upper()
        product, created = Product.objects.get_or_create(product_name=product_name_upper,refectory_id=self.kwargs['refectory_id'])
        form.data._mutable = True
        form.data['product_cod'] = product.id
        form.data._mutable = False

        if form.is_valid():
            return self.form_valid(form, product, created)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, product, created):
        self.object = form.save(commit=False)
        self.object.product_name = product.product_name
        self.object.product_total_amount = self.object.product_quantity * self.object.product_unitary_amount
        #si no existia el producto, se creo en el get or create
        if created:
            product.total_product_quantity = self.object.product_quantity
            product.product_unit = self.object.product_unit
            product.created_by = self.request.user
            product.refectory_id = self.kwargs['refectory_id']
            product.is_spare_part = self.object.is_spare_part
        #ya existia el producto
        else:
            if self.object.operation_type == 'Ingreso':    
                product.total_product_quantity = product.total_product_quantity + self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.created_by = self.request.user
                product.refectory_id = self.kwargs['refectory_id']
                product.is_spare_part = self.object.is_spare_part                    
            else:
                #si intento sacar mas de lo que hay
                if self.object.product_quantity > product.total_product_quantity:
                    return self.form_invalid(form)
                product.total_product_quantity = product.total_product_quantity - self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.created_by = self.request.user
                product.refectory_id = self.kwargs['refectory_id']
                product.is_spare_part = self.object.is_spare_part                

        product.save()
        self.object.created_by = self.request.user
        self.object.save()
        messages.success(self.request, 'Operación registrada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class ProductManagementCreateViewGuest(CreateView):
    model = ProductManagement
    queryset = ProductManagement.objects.all()
    form_class = ProductManagementForm
    template_name = "product_managements/product_management_create.html"
    success_url = "/dashboard/product-managements/operations"

    def get_context_data(self, **kwargs):
        context = super(ProductManagementCreateViewGuest, self).get_context_data(**kwargs)
        query = Product.objects.filter(refectory_id=self.request.user.profile.refectory.id).order_by('product_name')

        context['product_info'] = []
        context['product_operation'] = self.kwargs['op_type']
        for i in query:
            context['product_info'].append({
                "product_name": i.product_name,
                "product_quantity": i.total_product_quantity,
                "product_unit": i.product_unit,
            })

        context['refectory'] = {
            'id' : self.request.user.profile.refectory.id,
        }
        return context 

    def post(self, request, *args, **kwargs):

        self.object = None
        form = self.get_form()
        product_name_upper = form.data['product_cod'].upper()
        product, created = Product.objects.get_or_create(product_name=product_name_upper,refectory_id=self.request.user.profile.refectory.id)
        form.data._mutable = True
        form.data['product_cod'] = product.id
        form.data._mutable = False

        if form.is_valid():
            return self.form_valid(form, product, created)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, product, created):
        self.object = form.save(commit=False)
        self.object.product_name = product.product_name
        self.object.product_total_amount = self.object.product_quantity * self.object.product_unitary_amount
        #si no existia el producto, se creo en el get or create
        if created:
            product.total_product_quantity = self.object.product_quantity
            product.product_unit = self.object.product_unit
            product.created_by = self.request.user
            product.refectory_id = self.request.user.profile.refectory.id
            product.is_spare_part = self.object.is_spare_part
        #ya existia el producto
        else:
            if self.object.operation_type == 'Ingreso':    
                product.total_product_quantity = product.total_product_quantity + self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.created_by = self.request.user
                product.refectory_id = self.request.user.profile.refectory.id
                product.is_spare_part = self.object.is_spare_part                  
            else:
                #si intento sacar mas de lo que hay
                if self.object.product_quantity > product.total_product_quantity:
                    return self.form_invalid(form)
                product.total_product_quantity = product.total_product_quantity - self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.created_by = self.request.user
                product.refectory_id = self.request.user.profile.refectory.id
                product.is_spare_part = self.object.is_spare_part                

        product.save()
        self.object.created_by = self.request.user
        self.object.save()
        messages.success(self.request, 'Operación registrada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

@method_decorator([login_required, superuser_required], name='dispatch')
class ProductManagementUpdateView(UpdateView):
    form_class = ProductManagementForm
    model = ProductManagement 
    queryset = ProductManagement.objects.all()
    template_name = "product_managements/product_management_update.html"

    def get_success_url(self):
        success_url = reverse('dashboard:product_managements:list_product_management',kwargs={'refectory_id':self.kwargs['refectory_id']})    
        return success_url
    
    def get_context_data(self, **kwargs):

        context = super(ProductManagementUpdateView, self).get_context_data(**kwargs)
        product_info = Product.objects.filter(refectory_id=self.kwargs['refectory_id']).order_by('product_name')
        product_operation = ProductManagement.objects.filter(product_cod_id=context['object'].product_cod_id)

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
        product = Product.objects.get(product_name=self.object.product_name,refectory_id=self.kwargs['refectory_id'])
        self.object.product_cod = product
        
        #validaciones
        # si no se cambia el tipo de operacion
        if temp_operation == self.object.operation_type:
            if self.object.operation_type == 'Ingreso':
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # restar litros ingresados antiguos     
                product.total_product_quantity = (product.total_product_quantity - temp) + self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.is_spare_part = self.object.is_spare_part
            else:
                # sumar litros egresados antiguos                
                product.total_product_quantity = (product.total_product_quantity + temp) - self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.is_spare_part = self.object.is_spare_part
        #si cambia el tipo de operacion en la edicion
        else:
            if self.object.operation_type == 'Ingreso':
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # operacion inversa     
                product.total_product_quantity = (product.total_product_quantity + temp) + self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.is_spare_part = self.object.is_spare_part
            else:
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # operacion inversa                
                product.total_product_quantity = (product.total_product_quantity - temp) - self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.is_spare_part = self.object.is_spare_part                       
        product.save()
        messages.success(self.request, 'Operación actualizada exitosamente')
        return super().form_valid(form)



    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class ProductManagementUpdateViewGuest(UpdateView):
    form_class = ProductManagementForm
    model = ProductManagement 
    queryset = ProductManagement.objects.all()
    template_name = "product_managements/product_management_update.html"
    success_url = "/dashboard/product-managements/operations"
    
    def get_context_data(self, **kwargs):

        context = super(ProductManagementUpdateViewGuest, self).get_context_data(**kwargs)
        product_info = Product.objects.filter(refectory_id=self.request.user.profile.refectory.id).order_by('product_name')
        product_operation = ProductManagement.objects.filter(product_cod_id=context['object'].product_cod_id)

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
        product = Product.objects.get(product_name=self.object.product_name,refectory_id=self.request.user.profile.refectory.id)
        self.object.product_cod = product
        
        #validaciones
        # si no se cambia el tipo de operacion
        if temp_operation == self.object.operation_type:
            if self.object.operation_type == 'Ingreso':
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # restar litros ingresados antiguos     
                product.total_product_quantity = (product.total_product_quantity - temp) + self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.is_spare_part = self.object.is_spare_part
            else:
                # sumar litros egresados antiguos                
                product.total_product_quantity = (product.total_product_quantity + temp) - self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.is_spare_part = self.object.is_spare_part
        #si cambia el tipo de operacion en la edicion
        else:
            if self.object.operation_type == 'Ingreso':
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # operacion inversa     
                product.total_product_quantity = (product.total_product_quantity + temp) + self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.is_spare_part = self.object.is_spare_part
            else:
                if self.object.product_quantity < 0:
                    return self.form_invalid(form)
                # operacion inversa                
                product.total_product_quantity = (product.total_product_quantity - temp) - self.object.product_quantity
                product.product_unit = self.object.product_unit
                product.is_spare_part = self.object.is_spare_part                       
        product.save()
        messages.success(self.request, 'Operación actualizada exitosamente')
        return super().form_valid(form)



    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class ModalTemplate(TemplateView):
    template_name = "product_managements/product_management_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = ProductManagement.objects.get(pk=self.kwargs['pk'])
        product = Product.objects.get(pk=query.product_cod.id)
        
        context['operation'] = {
            'id':query.id,
            'type':query.operation_type,
            'product_name':query.product_name,
            'product_quantity':query.product_quantity,
            'product_unit':query.product_unit,
            'created':query.created,
            'product_total_quantity':product.total_product_quantity,
            'refectory_id':self.kwargs['refectory_id'],
        }
        return context

def DeleteProductManagementOperation(request, refectory_id, pk):
    product_op = get_object_or_404(ProductManagement, id = pk)
    product = Product.objects.get(pk=product_op.product_cod.id)
    #product = Product.objects.get(product_name=product_op.product_name,refectory_id=refectory_id)

    if product_op.operation_type == 'Ingreso':
        if product.total_product_quantity - product_op.product_quantity < 0:
            #TODO return a lista de operaciones y mensaje de error
            messages.error(request, 'No se puede eliminar la operación seleccionada')
            return HttpResponseRedirect("/dashboard/product-managements/"+str(refectory_id))
        product.total_product_quantity -= product_op.product_quantity


    else:
        product.total_product_quantity += product_op.product_quantity

    product.save()
    if product.total_product_quantity == 0:
        product.delete()
    
    product_op.delete()
    messages.success(request, 'Operación eliminada exitosamente')
    return HttpResponseRedirect("/dashboard/product-managements/"+str(refectory_id))