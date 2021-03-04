from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponse


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

from .forms import WaterManagementForm
from apps.dashboard.refectories.forms import WaterTankForm, WaterExtraFieldsForm

from apps.main.refectories.models import Refectory
from apps.main.users.models import CustomUser
from apps.main.water_tanks.models import WaterTank
from apps.main.water_managements.models import WaterManagement

@method_decorator([login_required, superuser_required], name='dispatch')
class WaterManagementList(ListView):
    template_name = "water_managements/list_water_managements.html"
    queryset = WaterManagement.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        tank = WaterTank.objects.get(id=self.kwargs['pk'])
        refectory = Refectory.objects.get(id=tank.refectory_id)
        query = WaterManagement.objects.filter(cupboard=tank.id).order_by('created')
        
        context['object_list'] = []
        context['tank_id'] = self.kwargs['pk']
        context['refectory_data'] = []

        for i in query:
            context['object_list'].append({
                    'id':i.id,
                    'date':i.created,
                    'operation_type':i.operation_type,
                    'operation_description':i.operation_description,
                    'water_liters':i.water_liters,
                    'water_amount':i.water_amount,
                    'water_price_total':i.water_price_total,
                    'created_by':str(i.created_by.profile.name) + ' ' + str(i.created_by.profile.last_name),
                    'created':i.created,
                    'tank_id':i.cupboard_id,
            })

        context['refectory_data'].append({
            'id':refectory.id,
            'refectory_name': refectory.name,
            'refectory_address': refectory.address,
            })

        if 'water_tank_form' not in context:
            
            context['water_tank_form'] = WaterTankForm(
                instance = tank,
                initial = {
                    'capacity':tank.capacity,
                    'current_liters':tank.current_liters,
                }
            )
            context['water_extra_fields'] = WaterExtraFieldsForm(
                initial = {'water_percent':(tank.current_liters * 100)//tank.capacity,
                })

        return context


class WaterManagementListGuest(ListView):
    template_name = "water_managements/list_water_managements.html"
    queryset = WaterManagement.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        refectory = Refectory.objects.get(id=self.request.user.profile.refectory.id)
        tank = WaterTank.objects.get(refectory_id=refectory.id)
        query = WaterManagement.objects.filter(cupboard=tank.id).order_by('created')
        
        context['object_list'] = []
        context['tank_id'] = tank.id
        context['refectory_data'] = []

        for i in query:
            context['object_list'].append({
                    'id':i.id,
                    'date':i.created,
                    'operation_type':i.operation_type,
                    'operation_description':i.operation_description,
                    'water_liters':i.water_liters,
                    'water_amount':i.water_amount,
                    'water_price_total':i.water_price_total,
                    'created_by':str(i.created_by.profile.name) + ' ' + str(i.created_by.profile.last_name),
                    'created':i.created,
                    'tank_id':i.cupboard_id,
            })

        context['refectory_data'].append({
            'id':refectory.id,
            'refectory_name': refectory.name,
            'refectory_address': refectory.address,
            })
        
        if 'water_tank_form' not in context:
            
            context['water_tank_form'] = WaterTankForm(
                instance = tank,
                initial = {
                    'capacity':tank.capacity,
                    'current_liters':tank.current_liters,
                }
            )
            context['water_extra_fields'] = WaterExtraFieldsForm(
                initial = {'water_percent':(tank.current_liters * 100)//tank.capacity,
                })

        return context

@method_decorator([login_required, superuser_required], name='dispatch')
class WaterManagementCreateView(CreateView):
    model = WaterManagement
    form_class = WaterManagementForm
    template_name = "water_managements/water_managements-create.html"
    
    def get_success_url(self):
        if self.request.user.is_superuser:
            success_url = "/dashboard/water_tanks/"
        else:
            success_url = "/dashboard/water_tanks/tank/"   
        return success_url

    def get_context_data(self, **kwargs):
        context = super(WaterManagementCreateView, self).get_context_data(**kwargs)

        query = WaterTank.objects.get(id=self.kwargs['tank_id'])
        
        context['tank_info'] = {
            'id' : self.kwargs['tank_id'],
            'capacity' : query.capacity,
            'current_liters' : query.current_liters,
            'sell_operation': False,
            'operation': self.kwargs['op_type'],
        }

        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.water_price_total = self.object.water_liters * self.object.water_amount
        self.object.cupboard_id = self.kwargs['tank_id']
        tank = WaterTank.objects.get(id=self.kwargs['tank_id'])
        #validaciones
        if self.object.operation_type == 'Ingreso':
            if self.object.water_liters > tank.capacity:
                return self.form_invalid(form)    
            tank.current_liters = tank.current_liters + self.object.water_liters    
            tank.last_fill_date = self.object.created
        else:
            if self.object.water_liters > tank.current_liters:
                return self.form_invalid(form)                
            tank.current_liters = tank.current_liters - self.object.water_liters    
        tank.save()
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class WaterManagementCreateViewGuest(CreateView):
    model = WaterManagement
    form_class = WaterManagementForm
    template_name = "water_managements/water_managements-create.html"
    success_url = "/dashboard/water_managements/operations"


    def get_context_data(self, **kwargs):
        context = super(WaterManagementCreateViewGuest, self).get_context_data(**kwargs)

        query = WaterTank.objects.get(refectory_id=self.request.user.profile.refectory.id)
        
        context['tank_info'] = {
            'id' : query.id,
            'capacity' : query.capacity,
            'current_liters' : query.current_liters,
            'operation': self.kwargs['op_type'],
            'sell_operation': False,
        }

        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.water_price_total = self.object.water_liters * self.object.water_amount
        tank = WaterTank.objects.get(refectory_id=self.request.user.profile.refectory.id)
        self.object.cupboard = tank
        #validaciones
        if self.object.operation_type == 'Ingreso':
            if self.object.water_liters > tank.capacity:
                return self.form_invalid(form)    
            tank.current_liters = tank.current_liters + self.object.water_liters    
            tank.last_fill_date = self.object.created
        else:
            if self.object.water_liters > tank.current_liters:
                return self.form_invalid(form)                
            tank.current_liters = tank.current_liters - self.object.water_liters    
        tank.save()
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        ) 

class WaterManagementRegisterSell(CreateView):
    model = WaterManagement
    form_class = WaterManagementForm
    template_name = "water_managements/water_managements-create.html"
    success_url = "/dashboard/water_managements/operations"

    def get_context_data(self, **kwargs):
        context = super(WaterManagementRegisterSell, self).get_context_data(**kwargs)

        query = WaterTank.objects.get(refectory_id=self.request.user.profile.refectory.id)
        
        context['tank_info'] = {
            'id' : query.id,
            'capacity' : query.capacity,
            'current_liters' : query.current_liters,
            'operation': 1,
            'sell_operation': True,
            'sell_price': query.refectory.capacity,
        }

        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.water_price_total = self.object.water_liters * self.object.water_amount
        self.object.cupboard_id = self.request.user.profile.refectory.id
        tank = WaterTank.objects.get(refectory_id=self.request.user.profile.refectory.id)
        #validaciones
        if self.object.water_liters > tank.current_liters:
            return self.form_invalid(form)                
        tank.current_liters = tank.current_liters - self.object.water_liters    
        tank.save()
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        ) 
        
@method_decorator([login_required, superuser_required], name='dispatch')
class WaterManagementUpdateView(UpdateView):
    form_class = WaterManagementForm
    model = WaterManagement 
    queryset = WaterManagement.objects.all()
    template_name = "water_managements/water_managements-update.html"

    def get_success_url(self):
        if self.request.user.is_superuser:
            success_url = "/dashboard/water_tanks/"
        else:
            success_url = "/dashboard/water_managements/operations"
        return success_url

    def get_context_data(self, **kwargs):

        context = super(WaterManagementUpdateView, self).get_context_data(**kwargs)
        water_operation = get_object_or_404(WaterManagement, pk=self.kwargs['pk'])
        query = WaterTank.objects.get(id=self.kwargs['tank_id'])
        context['tank_info'] = {
            'id' : self.kwargs['tank_id'],
            'capacity' : query.capacity,
            'current_liters' : query.current_liters,
        }        
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        temp = self.object.water_liters #valor actual
        temp_operation = self.object.operation_type
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form, temp, temp_operation)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, temp, temp_operation):
        self.object = form.save(commit=False)
        self.object.water_price_total = self.object.water_liters * self.object.water_amount
        tank = WaterTank.objects.get(id=self.kwargs['tank_id'])
        #validaciones
        # si no se cambia el tipo de operacion
        if temp_operation == self.object.operation_type:
            if self.object.operation_type == 'Ingreso':
                if self.object.water_liters > tank.capacity:
                    return self.form_invalid(form)
                # restar litros ingresados antiguos     
                tank.current_liters = (tank.current_liters - temp) + self.object.water_liters
            else:
                if self.object.water_liters > tank.current_liters:
                    return self.form_invalid(form)
                # sumar litros egresados antiguos                
                tank.current_liters = (tank.current_liters + temp) - self.object.water_liters
        #si cambia el tipo de operacion en la edicion
        else:
            if self.object.operation_type == 'Ingreso':
                if self.object.water_liters > tank.capacity:
                    return self.form_invalid(form)
                # operacion inversa     
                tank.current_liters = (tank.current_liters + temp) + self.object.water_liters
            else:
                if self.object.water_liters > tank.current_liters:
                    return self.form_invalid(form)
                # operacion inversa                
                tank.current_liters = (tank.current_liters - temp) - self.object.water_liters                        
        tank.save()
        return super().form_valid(form)


class WaterManagementUpdateViewGuest(UpdateView):
    form_class = WaterManagementForm
    model = WaterManagement 
    queryset = WaterManagement.objects.all()
    template_name = "water_managements/water_managements-update.html"
    success_url = "/dashboard/water_managements/operations"

    def get_context_data(self, **kwargs):

        context = super(WaterManagementUpdateViewGuest, self).get_context_data(**kwargs)

        query = WaterTank.objects.get(refectory_id=self.request.user.profile.refectory.id)

        context['tank_info'] = {
            'id' : query.id,
            'capacity' : query.capacity,
            'current_liters' : query.current_liters,
        }        
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        temp = self.object.water_liters #valor actual
        temp_operation = self.object.operation_type
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form, temp, temp_operation)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, temp, temp_operation):
        self.object = form.save(commit=False)
        self.object.water_price_total = self.object.water_liters * self.object.water_amount
        tank = WaterTank.objects.get(refectory_id=self.request.user.profile.refectory.id)
        #validaciones
        # si no se cambia el tipo de operacion
        if temp_operation == self.object.operation_type:
            if self.object.operation_type == 'Ingreso':
                if self.object.water_liters > tank.capacity:
                    return self.form_invalid(form)
                # restar litros ingresados antiguos     
                tank.current_liters = (tank.current_liters - temp) + self.object.water_liters
            else:
                if self.object.water_liters > tank.current_liters:
                    return self.form_invalid(form)
                # sumar litros egresados antiguos                
                tank.current_liters = (tank.current_liters + temp) - self.object.water_liters
        #si cambia el tipo de operacion en la edicion
        else:
            if self.object.operation_type == 'Ingreso':
                if self.object.water_liters > tank.capacity:
                    return self.form_invalid(form)
                # operacion inversa     
                tank.current_liters = (tank.current_liters + temp) + self.object.water_liters
            else:
                if self.object.water_liters > tank.current_liters:
                    return self.form_invalid(form)
                # operacion inversa                
                tank.current_liters = (tank.current_liters - temp) - self.object.water_liters                        
        tank.save()
        return super().form_valid(form)



    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )


def DeleteWaterOperation(request,pk):
    water_op = get_object_or_404(WaterManagement, id = pk)
    tank = WaterTank.objects.get(id=water_op.cupboard.id)
    last_filled = WaterManagement.objects.exclude(id=water_op.id).filter(operation_type='Ingreso', cupboard=tank).order_by('-created')

    if water_op.operation_type == 'Ingreso':
        tank.current_liters -= water_op.water_liters
        tank.last_fill_date = last_filled[0].created

    else:
        tank.current_liters += water_op.water_liters

    tank.save()

    water_op.delete()
    return HttpResponseRedirect("/dashboard/water_managements/"+str(tank.id))

    