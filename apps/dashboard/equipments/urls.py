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
        'list', 
        views.EquipmentsListViewGuest.as_view(), 
        name='list_equipments_guest'
        ),

    path(
        '<int:refectory_id>/<int:pk>/detail', 
        views.EquipmentDetailView.as_view(), 
        name='detail_equipments'
        ),

    path(
        '<int:pk>/detail', 
        views.EquipmentDetailViewGuest.as_view(), 
        name='detail_equipments_guest'
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

    path(
        '<int:refectory_id>/<int:pk>/delete', 
        views.EquipmentDeleteView.as_view(), 
        name='delete_equipments'
        ),

    path(
        '<int:refectory_id>/report',
        views.ModalTemplateReport.as_view(),
        name='equipments_report_modal'
    ),

    path(
        '<int:refectory_id>/pdf',
        views.DownloadPDF.as_view(),
        name='equipments_pdf'
    ),

]