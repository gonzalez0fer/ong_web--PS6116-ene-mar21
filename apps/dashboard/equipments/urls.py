from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "equipments"

urlpatterns = [
    path(
        '<int:refectory_id>', 
        views.EquipmentsListView.as_view(), 
        name='list_equipments'
        ),

    path(
        '<int:refectory_id>/create', 
        views.EquipmentCreateView.as_view(), 
        name='create_equipments'
        ),

    path(
        '<int:refectory_id>/<int:pk>/update', 
        views.EquipmentUpdateView.as_view(), 
        name='update_equipments'
        ),

]