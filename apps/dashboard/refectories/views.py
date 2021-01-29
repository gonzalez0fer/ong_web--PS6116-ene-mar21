from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView 
from django.http import HttpResponse

from apps.main.refectories.models import Refectory
from apps.main.users.models import UserProfile


class RefectoriesList(ListView):
    template_name = "refectories/refectory_list.html"
    queryset = Refectory.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
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

            print('HOLA',mandated)
            context['object_list'].append({'id':i.id, 'name':i.name, 
            'address':i.address, 'capacity':i.capacity,'mandated':mandated })
        return context  