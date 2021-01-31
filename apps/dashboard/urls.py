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
        'supplier/',
        include('apps.dashboard.suppliers.urls', namespace='suppliers'),
        ),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]