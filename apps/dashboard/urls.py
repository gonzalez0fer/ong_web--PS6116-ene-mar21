from django.conf.urls import include, url
from django.urls import path, re_path
from apps.dashboard import views

app_name = 'dashboard'

urlpatterns = [

    path(
        'user/',
        include('apps.dashboard.users.urls', namespace='users'),
        ),

    path(
        'refectory/',
        include('apps.dashboard.refectories.urls', namespace='refectories'),
        ),

    path(
        'cupboard/',
        include('apps.dashboard.cupboards.urls', namespace='cupboards'),
        ),

    path(
        'cupboard-management/',
        include('apps.dashboard.cupboard_managements.urls', namespace='cupboard_managements'),
        ),

    path(
        'supplier/',
        include('apps.dashboard.suppliers.urls', namespace='suppliers'),
        ),

    path(
        'water_tanks/',
        include('apps.dashboard.water_tanks.urls', namespace='water_tanks'),
        ),

    path(
        'water_managements/',
        include('apps.dashboard.water_managements.urls', namespace='water_managements'),
        ),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]