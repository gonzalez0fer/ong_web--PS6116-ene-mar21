from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponse
from django.contrib import messages

from .forms import RefectoryForm, WaterTankForm, WaterExtraFieldsForm
from apps.main.refectories.models import Refectory
from apps.main.users.models import CustomUser


class RefectoriesListView(ListView):
    template_name = "refectories/refectory_list.html"
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


class RefectoryCreateView(CreateView):
    model = Refectory
    queryset = Refectory.objects.all()
    form_class = RefectoryForm
    template_name = "refectories/refectory-create.html"
    success_url = "/dashboard/refectory/"

    def get_context_data(self, **kwargs):

        context = super(RefectoryCreateView, self).get_context_data(**kwargs)

        if 'water_tank_form' not in context:
            context['water_tank_form'] = WaterTankForm()
        return context

    def post(self, request, *args, **kwargs):

        self.object = None
        form = self.get_form()

        water_tank_form = WaterTankForm(request.POST)
        
        if form.is_valid() and water_tank_form.is_valid():
            return self.form_valid(form, water_tank_form)
        else:
            return self.form_invalid(form, water_tank_form)

    def form_valid(self, form, water_tank_form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()

        water_tank_object = water_tank_form.save(commit=False)
        water_tank_object.refectory = self.object
        water_tank_object.created_by = self.request.user
        water_tank_object.save()
        messages.success(self.request, 'Punto de distribución creado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form, water_tank_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                water_tank_form=water_tank_form,
            )
        )


class RefectoryUpdateView(UpdateView):
    form_class = RefectoryForm
    model = Refectory 
    queryset = Refectory.objects.all()
    template_name = "refectories/refectory-edit.html"
    success_url = "/dashboard/refectory/"

    def get_context_data(self, **kwargs):

        context = super(RefectoryUpdateView, self).get_context_data(**kwargs)

        refectory = get_object_or_404(Refectory, pk=self.kwargs['pk'])

        try:
            water_tank = refectory.water_tank
        except:
            water_tank = None

        if 'water_tank_form' not in context:
            
            context['water_tank_form'] = WaterTankForm(
                instance = water_tank,
                initial = {
                    'capacity':water_tank.capacity,
                    'current_liters':water_tank.current_liters,
                }
            )
            context['water_extra_fields'] = WaterExtraFieldsForm(
                initial = {'water_percent':(water_tank.current_liters * 100)//water_tank.capacity,
                })

        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()

        water_tank_form = WaterTankForm(
            request.POST,
            instance = self.object.water_tank
        )

        if form.is_valid() and water_tank_form.is_valid():
            return self.form_valid(form, water_tank_form)
        else:
            return self.form_invalid(form, water_tank_form)

    def form_valid(self, form, water_tank_form):
        self.object = form.save(commit=False)
        self.object.water_tank.capacity = water_tank_form.cleaned_data['capacity']
        self.object.water_tank.current_liters = water_tank_form.cleaned_data['current_liters']
        self.object.water_tank.save()
        messages.success(self.request, 'Punto de distribución actualizado exitosamente')
        return super().form_valid(form)



    def form_invalid(self, form, water_tank_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                water_tank_form=water_tank_form
            )
        )