from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponse

from apps.main.suppliers.models import Supplier
from .forms import SupplierForm

class SuppliersListView(ListView):
    template_name = "suppliers/supplier_list.html"
    queryset = Supplier.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = Supplier.objects.order_by('id')
        
        context['object_list'] = []

        for i in query:
            context['object_list'].append({'id':i.id, 'company_name':i.company_name, 
            'company_contact_name':i.company_contact_name, 'company_rif':i.company_rif,
            'company_address':i.company_address, 'company_phone':i.company_phone,
            'company_description':i.company_description,})

        return context  


class SupplierCreateView(CreateView):
    model = Supplier
    queryset = Supplier.objects.all()
    form_class = SupplierForm
    template_name = "suppliers/supplier-create.html"
    success_url = "/dashboard/supplier/"

    def get_context_data(self, **kwargs):

        context = super(SupplierCreateView, self).get_context_data(**kwargs)
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
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
            )
        )

class SupplierUpdateView(UpdateView):
    form_class = SupplierForm
    model = Supplier 
    queryset = Supplier.objects.all()
    template_name = "suppliers/supplier-edit.html"
    success_url = "/dashboard/supplier/"

    def get_context_data(self, **kwargs):

        context = super(SupplierUpdateView, self).get_context_data(**kwargs)
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