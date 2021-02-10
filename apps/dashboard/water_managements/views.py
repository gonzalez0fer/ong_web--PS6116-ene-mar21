from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponse


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

from .forms import WaterManagementForm

from apps.main.refectories.models import Refectory
from apps.main.users.models import CustomUser
from apps.main.water_tanks.models import WaterTank
from apps.main.water_managements.models import WaterManagement


class WaterManagementList(ListView):
    template_name = "water_managements/list_water_managements.html"
    queryset = WaterManagement.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        tank = WaterTank.objects.get(id=self.kwargs['pk'])
        query = WaterManagement.objects.filter(cupboard=tank.id).order_by('created')
        
        context['object_list'] = []

        for i in query:
            
            context['object_list'].append({
                    'id':i.id,
                    'date':i.created,
                    'operation_type':i.operation_type,
                    'water_liters':i.water_liters,
                    'water_amount':i.water_amount,
                    'created_by_id':i.created_by_id,
                    'created':i.created,
                    'tank_id':i.cupboard_id,
            })
        return context

class WaterManagementCreateView(CreateView):
    model = WaterManagement
    form_class = WaterManagementForm
    template_name = "water_managements/water_managements-create.html"
    success_url = "/dashboard/water_tanks/"

    def get_context_data(self, **kwargs):
        context = super(WaterManagementCreateView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by_id = self.request.user.id
        self.object.cupboard_id = 1 #provisional hasta que se pueda asignar comedores a usuarios
        #validaciones
        self.object.save()
        # water_tank_object = water_tank_form.save(commit=False)
        # water_tank_object.refectory = self.object
        # water_tank_object.created_by = self.request.user
        # water_tank_object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        ) 