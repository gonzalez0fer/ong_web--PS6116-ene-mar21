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
]