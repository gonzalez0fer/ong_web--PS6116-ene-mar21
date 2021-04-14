from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Avg, Sum

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

from apps.main.refectories.models import Refectory
from apps.main.equipments.models import Equipment
from apps.main.products.models import Product
from apps.main.maintenance.models import Maintenance
from .forms import EquipmentForm

from apps.main.utils import render_pdf_view
from datetime import datetime, timedelta

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
    template_name = "equipments/equipment_details.html"

class EquipmentDetailViewGuest(DetailView):
    model = Equipment
    template_name = "equipments/equipment_details.html"


@method_decorator([login_required, superuser_required], name='dispatch')
class EquipmentCreateView(CreateView):
    model = Equipment
    queryset = Equipment.objects.all()
    form_class = EquipmentForm
    template_name = "equipments/equipment_create.html"
    
    def get_success_url(self, **kwargs):
        success_url = reverse('dashboard:equipments:list_equipments',kwargs={'refectory_id':self.kwargs['refectory_id']})
        return success_url

    def get_context_data(self, **kwargs):

        context = super(EquipmentCreateView, self).get_context_data(**kwargs)

        query = Product.objects.filter(refectory_id=self.kwargs['refectory_id'],is_spare_part=True)

        context['spare_info'] = []
        
        for i in query:
            context['spare_info'].append({
            'id':i.id,
            'product_name': i.product_name,
            })

        context['refectory'] = {
            'id' : self.kwargs['refectory_id'],
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
        self.object.refectory_id = self.kwargs['refectory_id']
        self.object.save()
        messages.success(self.request, 'Equipo registrado exitosamente')
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
        success_url = reverse('dashboard:equipments:list_equipments',kwargs={'refectory_id':self.kwargs['refectory_id']})
        return success_url

    def get_context_data(self, **kwargs):

        context = super(EquipmentUpdateView, self).get_context_data(**kwargs)

        query = Product.objects.filter(refectory_id=self.kwargs['refectory_id'],is_spare_part=True)

        context['spare_info'] = []
        
        for i in query:
            context['spare_info'].append({
            'id':i.id,
            'product_name': i.product_name,
            })

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
        messages.success(self.request, 'Equipo actualizado exitosamente')
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
        success_url = reverse('dashboard:equipments:list_equipments',kwargs={'refectory_id':self.kwargs['refectory_id']})
        messages.success(self.request, 'Equipo eliminado exitosamente')
        return success_url
    
    def get_context_data(self, **kwargs):

        context = super(EquipmentDeleteView, self).get_context_data(**kwargs)

        context['refectory'] = {
            'id' : self.kwargs['refectory_id'],
        }
        return context

class ModalTemplateReport(TemplateView):
    template_name = "equipments/report_modal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['refectory_id'] = self.kwargs['refectory_id']

        return context

class DownloadPDF(View):

    def get(self, request, *args, **kwargs):
		
        refectory = Refectory.objects.get(id=self.kwargs['refectory_id'])

        from_date = self.request.GET.get("from_date")
        to_date = self.request.GET.get("to_date")

        new_from_date =  datetime.strptime(from_date, "%Y-%m-%d")
        new_from_date_str = datetime.strftime(new_from_date, "%d-%m-%Y")
         
        new_to_date =  datetime.strptime(to_date, "%Y-%m-%d")
        #Sumar 1 a to_date porque el query se realiza hasta las 00:00 del dia seleccionado
        new_to_date_1 = new_to_date + timedelta(days=1)
        new_to_date_1_str = datetime.strftime(new_to_date_1, "%Y-%m-%d")
        new_to_date_str = datetime.strftime(new_to_date, "%d-%m-%Y")

        query = Equipment.objects.filter(refectory_id=self.kwargs['refectory_id'])
        if not query:
            messages.error(self.request, 'No existen equipos registrados para generar reporte')
            return HttpResponseRedirect("/dashboard/equipments/"+str(self.kwargs['refectory_id']))
        
        count = 0
        equipments_maintenance = {}

        for i in query:
            operations = Maintenance.objects.filter(equipment_id=i.id, created__range=(from_date,new_to_date_1_str))
            if operations:
                count += len(operations)
                equipments_maintenance[i.name] = len(operations)
            else:
                pass

        if count == 0:
            messages.error(self.request, 'No existen mantenimientos en el periodo seleccionado')
            return HttpResponseRedirect("/dashboard/equipments/"+str(self.kwargs['refectory_id']))

        data = {
            "nombre": refectory.name,
            "direccion": refectory.address,
            "desde": new_from_date_str,
            "hasta": new_to_date_str,
            "mantenimientos": equipments_maintenance,
            "total_operaciones": count,
            "numero_equipos": len(query),
        }

        pdf = render_pdf_view('equipments/pdf_equipments.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Reporte Equipos.pdf" #TODO nombre dinamico
        content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response