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

    path(           
        'maintenance/',
        include('apps.dashboard.maintenance.urls', namespace='maintenance'),
        ),

    path(
        'products/',
        include('apps.dashboard.products.urls', namespace='products'),
        ),

    path(
        'product-managements/',
        include('apps.dashboard.product_managements.urls', namespace='product_managements'),
        ),

    path(
        'equipments/',
        include('apps.dashboard.equipments.urls', namespace='equipments'),
        ),

    path(
        'notifications-panel/',
        include('apps.dashboard.notifications.urls', namespace='notifications'),
        ),
   
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]