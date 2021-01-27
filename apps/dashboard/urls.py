from django.conf.urls import include, url
from django.urls import path, re_path
from apps.dashboard import views

app_name = 'dashboard'

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path(
        'user/',
        include('apps.dashboard.users.urls', namespace='users'),
        ),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]