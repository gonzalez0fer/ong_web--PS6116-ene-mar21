# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, index
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    # The home page
    path('', RedirectView.as_view(url='dashboard/')),
    path('dashboard/', index, name='home'),
    path('login/', login_view, name="login"),
    path('dashboard/user/register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]
