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
        '<int:tank_id>/<int:op_type>/create', 
        views.WaterManagementCreateView.as_view(), 
        name='water_management_create'
        ),
    path(
        '<int:tank_id>/<int:pk>/update', 
        views.WaterManagementUpdateView.as_view(), 
        name='water_management_update'
        ),      

    path(
        '<int:pk>/delete', 
        views.DeleteWaterOperation, 
        name='water_management_delete'
        ),  
]