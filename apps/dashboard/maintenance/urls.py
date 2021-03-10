from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "maintenance"

urlpatterns = [

    path(
        'refectories', 
        views.RefectoriesMaintenanceListView.as_view(), 
        name='refectories_maintenance_list'
    ),

    path(
        '<int:refectory_id>/<int:pk>/history', 
        views.MaintenanceList.as_view(), 
        name='maintenance_list'
        ),

    path(
        '<int:pk>/history', 
        views.MaintenanceListGuest.as_view(), 
        name='maintenance_list_guest'
        ),

    path(
        '<int:refectory_id>/<int:pk>/register', 
        views.MaintenanceCreateView.as_view(), 
        name='maintenance_create'
        ),

    path(
        '<int:pk>/register', 
        views.MaintenanceCreateViewGuest.as_view(), 
        name='maintenance_create_guest'
        ),

    path(
        '<int:refectory_id>/<int:equipment_id>/<int:pk>/update', 
        views.MaintenanceUpdateView.as_view(), 
        name='maintenance_update'
        ),

    path(
        '<int:pk>/update', 
        views.MaintenanceUpdateViewGuest.as_view(), 
        name='maintenance_update_guest'
        ),

    path(
        '<int:refectory_id>/<int:pk>/delete', 
        views.DeleteMaintenance, 
        name='maintenance_delete'
        ),

]