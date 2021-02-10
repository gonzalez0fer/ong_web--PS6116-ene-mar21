from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "water_managements"

urlpatterns = [
    path(
        '<int:pk>', 
        views.WaterManagementList.as_view(), 
        name='water_management_list'
        ),
    path(
        'create/', 
        views.WaterManagementCreateView.as_view(), 
        name='water_management_create'
        ),    
]