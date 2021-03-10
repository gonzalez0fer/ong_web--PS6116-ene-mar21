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
        'operations', 
        views.WaterManagementListGuest.as_view(), 
        name='water_management_list_guest'
        ),

    path(
        '<int:tank_id>/<int:op_type>/create', 
        views.WaterManagementCreateView.as_view(), 
        name='water_management_create'
        ),

    path(
        'create/sell', 
        views.WaterManagementRegisterSell.as_view(), 
        name='water_management_sell'
        ),

    path(
        '<int:op_type>/create', 
        views.WaterManagementCreateViewGuest.as_view(), 
        name='water_management_create_guest'
        ),

    path(
        '<int:tank_id>/<int:pk>/update', 
        views.WaterManagementUpdateView.as_view(), 
        name='water_management_update'
        ),

    path(
        '<int:pk>/update', 
        views.WaterManagementUpdateViewGuest.as_view(), 
        name='water_management_update_guest'
        ),

    path(
        '<int:pk>/delete/modal', 
        views.ModalTemplate.as_view(), 
        name='water_management_modal'
        ), 

    path(
        '<int:pk>/delete', 
        views.DeleteWaterOperation, 
        name='water_management_delete'
        ),  
]