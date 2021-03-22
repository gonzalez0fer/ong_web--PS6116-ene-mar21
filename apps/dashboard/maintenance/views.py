from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

from .forms import MaintenanceForm
from apps.dashboard.product_managements.forms import ProductManagementForm
from apps.main.maintenance.models import Maintenance
from apps.main.refectories.models import Refectory
from apps.main.products.models import Product
from apps.main.product_managements.models import ProductManagement
from apps.main.equipments.models import Equipment

@method_decorator([login_required, superuser_required], name='dispatch')
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

@method_decorator([login_required, superuser_required], name='dispatch')
class MaintenanceList(ListView):
    template_name = "maintenance/maintenance_list.html"
    queryset = Maintenance.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        refectory = Refectory.objects.get(id=self.kwargs['refectory_id'])
        query = Maintenance.objects.filter(equipment=self.kwargs['pk']).order_by('created')
        equipment = Equipment.objects.get(id=self.kwargs['pk'])

        context['object_list'] = []
        context['refectory_data'] = []

        for i in query:
            if i.product == None:
                context['object_list'].append({
                        'id':i.id,
                        'equipment_name':i.equipment.name,
                        'activity':i.activity,
                        'comments':i.comments,
                        'product_name':"-",
                        'product_quantity':"-",
                        'created_by':str(i.created_by.profile.name) + ' ' + str(i.created_by.profile.last_name),
                        'created':i.created,
                })
            else:
                context['object_list'].append({
                        'id':i.id,
                        'equipment_name':i.equipment.name,
                        'activity':i.activity,
                        'comments':i.comments,
                        'product_name':i.product.product_name,
                        'product_quantity':i.product_quantity,
                        'created_by':str(i.created_by.profile.name) + ' ' + str(i.created_by.profile.last_name),
                        'created':i.created,
                })

        context['equipment_id'] = self.kwargs['pk']
        context['equipment_name'] = equipment.name

        context['refectory_data'].append({
            'id':refectory.id,
            'refectory_name': refectory.name,
            'refectory_address': refectory.address,
            })
        return context

class MaintenanceListGuest(ListView):
    template_name = "maintenance/maintenance_list.html"
    queryset = Maintenance.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        refectory = Refectory.objects.get(id=self.request.user.profile.refectory.id)
        query = Maintenance.objects.filter(equipment=self.kwargs['pk']).order_by('created')
        equipment = Equipment.objects.get(id=self.kwargs['pk'])
        
        context['object_list'] = []
        context['refectory_data'] = []

        for i in query:
            if i.product == None:
                context['object_list'].append({
                        'id':i.id,
                        'equipment_name':i.equipment.name,
                        'activity':i.activity,
                        'comments':i.comments,
                        'product_name':"-",
                        'product_quantity':"-",
                        'created_by':str(i.created_by.profile.name) + ' ' + str(i.created_by.profile.last_name),
                        'created':i.created,
                })
            else:
                context['object_list'].append({
                        'id':i.id,
                        'equipment_name':i.equipment.name,
                        'activity':i.activity,
                        'comments':i.comments,
                        'product_name':i.product.product_name,
                        'product_quantity':i.product_quantity,
                        'created_by':str(i.created_by.profile.name) + ' ' + str(i.created_by.profile.last_name),
                        'created':i.created,
                })
        
        context['equipment_id'] = self.kwargs['pk']
        context['equipment_name'] = equipment.name

        context['refectory_data'].append({
            'id':refectory.id,
            'refectory_name': refectory.name,
            'refectory_address': refectory.address,
            })
        return context

@method_decorator([login_required, superuser_required], name='dispatch')
class MaintenanceCreateView(CreateView):
    model = Maintenance
    form_class = MaintenanceForm
    template_name = "maintenance/maintenance_create.html"
    
    def get_success_url(self):
        success_url = reverse('dashboard:maintenance:maintenance_list',kwargs={'refectory_id':self.kwargs['refectory_id'],'pk':self.kwargs['pk']})
        return success_url

    def get_context_data(self, **kwargs):
        context = super(MaintenanceCreateView, self).get_context_data(**kwargs)

        query = Product.objects.filter(refectory_id=self.kwargs['refectory_id']).order_by('product_name')
        
        context['product_info'] = []

        for i in query:
            context['product_info'].append({
                'product_name': i.product_name,
                'product_quantity': i.total_product_quantity,
            })

        context['refectory'] = {
            'id' : self.kwargs['refectory_id'],
            'equipment_id':self.kwargs['pk'],
        }

        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()


        try:
            product_used = Product.objects.get(refectory_id=self.kwargs['refectory_id'],product_name=form.data['product_name'])

        except ObjectDoesNotExist:
            product_used = None
            product_management_form = None
            if form.is_valid():
                return self.form_valid(form, product_management_form, product_used)
            else:
                return self.form_invalid(form)
        else:
            product_management_form = ProductManagementForm(
                data={
                    'product_cod':product_used,
                    'product_name':product_used.product_name,
                    'product_unit':product_used.product_unit,
                    'operation_type':'Egreso',
                    'product_quantity':form.data['product_quantity'],
                    'product_unitary_amount':0,
                    'is_spare_part':product_used.is_spare_part,
                    'is_maintenance':True,
            })

            if form.is_valid() and product_management_form.is_valid():
                return self.form_valid(form, product_management_form, product_used)
            else:
                return self.form_invalid(form)

    def form_valid(self, form, product_management_form, product_used):
        self.object = form.save(commit=False)
        self.object.equipment_id = self.kwargs['pk']
        self.object.created_by = self.request.user
        self.object.product = product_used
        
        if product_management_form != None:
            product_management_object = product_management_form.save(commit=False)
            product_management_object.product_total_amount = 0
            product_management_object.created_by = self.request.user
            
            #validacion de cantidad disponible
            product_used.total_product_quantity -= self.object.product_quantity 
            product_used.save()
            product_management_object.save()

            #buscar y guardar operacion registradad de product management
            self.object.product_operation = product_management_object
        else:
            self.object.product_operation = product_management_form

        self.object.save()
        messages.success(self.request, 'Mantenimiento registrado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class MaintenanceCreateViewGuest(CreateView):
    model = Maintenance
    form_class = MaintenanceForm
    template_name = "maintenance/maintenance_create.html"

    def get_success_url(self):
        success_url = reverse('dashboard:maintenance:maintenance_list_guest',kwargs={'pk':self.kwargs['pk']})
        return success_url

    def get_context_data(self, **kwargs):
        context = super(MaintenanceCreateViewGuest, self).get_context_data(**kwargs)

        query = Product.objects.filter(refectory_id=self.request.user.profile.refectory.id).order_by('product_name')
        
        context['product_info'] = []

        for i in query:
            context['product_info'].append({
                "product_name": i.product_name,
                "product_quantity": i.total_product_quantity,
            })

        context['refectory'] = {
            'id' : self.request.user.profile.refectory.id,
            'equipment_id':self.kwargs['pk'],
        }

        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()

        try:
            product_used = Product.objects.get(refectory_id=self.request.user.profile.refectory.id,product_name=form.data['product_name'])

        except ObjectDoesNotExist:
            product_used = None
            product_management_form = None
            if form.is_valid():
                return self.form_valid(form, product_management_form, product_used)
            else:
                return self.form_invalid(form)
        else:
            product_management_form = ProductManagementForm(
                data={
                    'product_cod':product_used,
                    'product_name':product_used.product_name,
                    'product_unit':product_used.product_unit,
                    'operation_type':'Egreso',
                    'product_quantity':form.data['product_quantity'],
                    'product_unitary_amount':0,
                    'is_spare_part':product_used.is_spare_part,
                    'is_maintenance':True,
            })

            if form.is_valid() and product_management_form.is_valid():
                return self.form_valid(form, product_management_form, product_used)
            else:
                return self.form_invalid(form)


    def form_valid(self, form, product_management_form, product_used):
        self.object = form.save(commit=False)
        self.object.equipment_id = self.kwargs['pk']
        self.object.created_by = self.request.user
        self.object.product = product_used
        
        if product_management_form != None:
            product_management_object = product_management_form.save(commit=False)
            product_management_object.product_total_amount = 0
            product_management_object.created_by = self.request.user
            
            #validacion de cantidad disponible
            product_used.total_product_quantity -= self.object.product_quantity 
            product_used.save()
            product_management_object.save()
            #buscar y guardar operacion registradad de product management
    
            self.object.product_operation = product_management_object
        
        else:
            self.object.product_operation = product_management_form

        self.object.save()
        messages.success(self.request, 'Mantenimiento registrado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

@method_decorator([login_required, superuser_required], name='dispatch')
class MaintenanceUpdateView(UpdateView):
    model = Maintenance
    form_class = MaintenanceForm
    template_name = "maintenance/maintenance_update.html"
    
    def get_success_url(self):
        success_url = reverse('dashboard:maintenance:maintenance_list',kwargs={'refectory_id':self.kwargs['refectory_id'],'pk':self.kwargs['equipment_id']})
        return success_url

    def get_context_data(self, **kwargs):
        context = super(MaintenanceUpdateView, self).get_context_data(**kwargs)

        if context['object'].product_operation != None:
            product_operation = ProductManagement.objects.get(id=context['object'].product_operation.id)        
            query = Product.objects.filter(refectory_id=self.kwargs['refectory_id']).order_by('product_name')
            
            context['product_info'] = []
            context['product_operation'] = product_operation

            for i in query:
                context['product_info'].append({
                    "product_name": i.product_name,
                    "product_quantity": i.total_product_quantity,
                })

            context['refectory'] = {
                'id' : self.kwargs['refectory_id'],
                'equipment_id':self.kwargs['equipment_id'],
            }
        else:
            context['refectory'] = {
                'id' : self.kwargs['refectory_id'],
                'equipment_id':self.kwargs['equipment_id'],
                'no_products_op':True,
            }

        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        temp = self.object.product_quantity
        form = self.get_form()
        try:
            product_used = Product.objects.get(refectory_id=self.kwargs['refectory_id'],product_name=form.data['product_name'])

        except ObjectDoesNotExist:
            product_used = None
            temp = None
        else:
            pass

        if form.is_valid():
            return self.form_valid(form, product_used, temp)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, product_used, temp):
        self.object = form.save(commit=False)
        

        if product_used != None:
            self.object.product = product_used
            product_management_object = ProductManagement.objects.get(id=self.object.product_operation.id)
            #TODO VALIDAR SI ES EL MISMO PRODUCTO O SE CAMBIO
            product_management_object.product_cod = product_used
            product_management_object.product_name = product_used.product_name
            product_management_object.product_quantity = self.object.product_quantity
            
            #TODO validacion de cantidad disponible
            product_used.total_product_quantity = (product_used.total_product_quantity + temp) - self.object.product_quantity 
            product_used.save()

            product_management_object.save()

        self.object.save()
        messages.success(self.request, 'Mantenimiento actualizado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class MaintenanceUpdateViewGuest(UpdateView):
    model = Maintenance
    form_class = MaintenanceForm
    template_name = "maintenance/maintenance_update.html"

    def get_success_url(self):
        query = Maintenance.objects.get(id=self.kwargs['pk'])
        success_url = reverse('dashboard:maintenance:maintenance_list_guest',kwargs={'pk':query.equipment.id})
        return success_url


    def get_context_data(self, **kwargs):
        context = super(MaintenanceUpdateViewGuest, self).get_context_data(**kwargs)

        if context['object'].product_operation != None:
            product_operation = ProductManagement.objects.get(id=context['object'].product_operation.id)
            query = Product.objects.filter(refectory_id=self.request.user.profile.refectory.id).order_by('product_name')

            context['product_info'] = []
            context['product_operation'] = product_operation

            for i in query:
                context['product_info'].append({
                    "product_name": i.product_name,
                    "product_quantity": i.total_product_quantity,
                })

            context['refectory'] = {
                'id' : self.request.user.profile.refectory.id,
                'equipment_id':context['object'].equipment.id,
            }

        else:
            context['refectory'] = {
                'id' : self.request.user.profile.refectory.id,
                'equipment_id':context['object'].equipment.id,
                'no_products_op':True,
            }

        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        temp = self.object.product_quantity
        form = self.get_form()

        try:
            product_used = Product.objects.get(refectory_id=self.request.user.profile.refectory.id,product_name=form.data['product_name'])

        except ObjectDoesNotExist:
            product_used = None
            temp = None
        else:
            pass

        if form.is_valid():
            return self.form_valid(form, product_used, temp)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, product_used, temp):
        self.object = form.save(commit=False)
        
        if product_used != None:
            self.object.product = product_used
            product_management_object = ProductManagement.objects.get(id=self.object.product_operation.id)
            #TODO VALIDAR SI ES EL MISMO PRODUCTO
            product_management_object.product_cod = product_used
            product_management_object.product_name = product_used.product_name
            product_management_object.product_quantity = self.object.product_quantity
            
            #TODO validacion de cantidad disponible
            product_used.total_product_quantity = (product_used.total_product_quantity + temp) - self.object.product_quantity 
            product_used.save()

            product_management_object.save()
        
        self.object.save()
        messages.success(self.request, 'Mantenimiento actualizado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class ModalTemplate(TemplateView):
    template_name = "maintenance/maintenance_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = Maintenance.objects.get(pk=self.kwargs['pk'])
        
        context['operation'] = {
            'id':query.id,
            'equipment_id':query.equipment.id,
            'activity':query.activity,
            'created':query.created,
            'refectory_id':self.kwargs['refectory_id'],
        }
        return context

def DeleteMaintenance(request, refectory_id, equipment_id, pk):
    maintenance_op = get_object_or_404(Maintenance, id = pk)

    if maintenance_op.product_operation != None:
        product_operation = ProductManagement.objects.get(id=maintenance_op.product_operation.id)
        product = Product.objects.get(refectory_id=refectory_id,product_name=product_operation.product_name)

        product.total_product_quantity += product_operation.product_quantity 
        product.save()    
        product_operation.delete()
    
    maintenance_op.delete()
    messages.success(request, 'Mantenimiento eliminado exitosamente')
    return HttpResponseRedirect("/dashboard/maintenance/"+str(refectory_id)+"/"+str(equipment_id)+"/history")
    