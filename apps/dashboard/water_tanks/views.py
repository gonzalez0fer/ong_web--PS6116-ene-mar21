from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponse

#from .forms import RefectoryForm, WaterTankForm, WaterExtraFieldsForm
from apps.main.water_tanks.models import WaterTank
from apps.main.users.models import CustomUser


class TanksListView(ListView):
    template_name = "water_tanks/tanks_list.html"
    queryset = WaterTank.objects.all()