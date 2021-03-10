from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

from apps.main.refectories.models import Refectory
from apps.main.equipments.models import Equipment
from apps.main.products.models import Product
from .forms import EquipmentForm

@method_decorator([login_required, superuser_required], name='dispatch')
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


class EquipmentsListViewGuest(ListView):
    template_name = "equipments/equipment_list.html"
    queryset = Equipment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        refectory = Refectory.objects.get(id=self.request.user.profile.refectory.id)
        query = Equipment.objects.filter(refectory_id=refectory.id)
        
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


@method_decorator([login_required, superuser_required], name='dispatch')
class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = ""

class EquipmentDetailViewGuest(DetailView):
    model = Equipment
    template_name = ""


@method_decorator([login_required, superuser_required], name='dispatch')
class EquipmentCreateView(CreateView):
    model = Equipment
    queryset = Equipment.objects.all()
    form_class = EquipmentForm
    template_name = "equipments/equipment_create.html"
    
    def get_success_url(self, **kwargs):
        succes_url = reverse('dashboard:equipments:list_equipments',kwargs={'refectory_id':self.kwargs['refectory_id']})
        return succes_url

    def get_context_data(self, **kwargs):

        context = super(EquipmentCreateView, self).get_context_data(**kwargs)

        query = Product.objects.filter(refectory_id=self.kwargs['refectory_id'],is_spare_part=True)

        context['spare_info'] = []
        
        for i in query:
            context['spare_info'].append({
            'product_name': i.product_name,
            })

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
        # Para cuando se incluya repuesto en el form de crear
        # spare_part = Product.objects.get(refectory_id=self.kwargs['refectory_id'],product_name=self.object.spare_part_name)
        # self.object.spare_part = spare_part
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

@method_decorator([login_required, superuser_required], name='dispatch')
class EquipmentUpdateView(UpdateView):
    form_class = EquipmentForm
    model = Equipment 
    queryset = Equipment.objects.all()
    template_name = "equipments/equipment_update.html"

    def get_success_url(self, **kwargs):
        succes_url = reverse('dashboard:equipments:list_equipments',kwargs={'refectory_id':self.kwargs['refectory_id']})
        return succes_url

    def get_context_data(self, **kwargs):

        context = super(EquipmentUpdateView, self).get_context_data(**kwargs)

        context['refectory'] = {
            'id' : self.kwargs['refectory_id'],
        }
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
        # Para cuando se incluya repuesto en el form de actualizar
        # spare_part = Product.objects.get(refectory_id=self.kwargs['refectory_id'],product_name=self.object.spare_part_name)
        # self.object.spare_part = spare_part
        return super().form_valid(form)


    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = "equipments/equipments_delete.html"

    def get_success_url(self, **kwargs):
        succes_url = reverse('dashboard:equipments:list_equipments',kwargs={'refectory_id':self.kwargs['refectory_id']})
        return succes_url
    
    def get_context_data(self, **kwargs):

        context = super(EquipmentDeleteView, self).get_context_data(**kwargs)

        context['refectory'] = {
            'id' : self.kwargs['refectory_id'],
        }
        return context
