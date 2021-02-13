from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "maintenance"

urlpatterns = [
    path(
        '', 
        views.MaintenanceListView.as_view(), 
        name='maintenance_list'
        ),
]