from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponse

from apps.main.refectories.models import Refectory
from apps.main.equipments.models import Equipment
from .forms import EquipmentForm

class EquipmentsListView(ListView):
    template_name = "equipments/equipment_list.html"
    queryset = Equipment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        refectory = Refectory.objects.get(id=self.kwargs['refectory_id'])
        query = Equipment.objects.filter(refectory_id=self.kwargs['refectory_id'])
        
        context['object_list'] = []
        context['refectory_data'] = []

        for i in query:
            context['object_list'].append({
                'id':i.id, 
                'equipment_name':i.name, 
                'equipment_brand':i.brand, 
                'equipment_frequency':i.maintenance_frequency,
            })

        context['refectory_data'].append({
            'id':refectory.id,
            'refectory_name': refectory.name,
            'refectory_address': refectory.address,
            })

        return context

class EquipmentCreateView(CreateView):
    model = Equipment
    queryset = Equipment.objects.all()
    form_class = EquipmentForm
    template_name = "equipments/equipment_create.html"
    success_url = "/dashboard"

    def get_context_data(self, **kwargs):

        context = super(EquipmentCreateView, self).get_context_data(**kwargs)
        context['refectory'] = {
            'id' : self.kwargs['refectory_id'],
        }
        return context

    def post(self, request, *args, **kwargs):

        self.object = None
        form = self.get_form()
        print(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.refectory_id = self.kwargs['refectory_id']
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class EquipmentUpdateView(UpdateView):
    form_class = EquipmentForm
    model = Equipment 
    queryset = Equipment.objects.all()
    template_name = ""
    success_url = "/dashboard"

    def get_context_data(self, **kwargs):

        context = super(EquipmentUpdateView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super().form_valid(form)


    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )  