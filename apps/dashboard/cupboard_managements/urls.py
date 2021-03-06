from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "cupboard-management"

urlpatterns = [
    path(
        'operations', 
        views.CupboardManagementListSingleView.as_view(), 
        name='list_cupboard_single_management'
        ),

    path(
        '<int:refectory_id>', 
        views.CupboardManagementListView.as_view(), 
        name='list_cupboard_management'
        ),

    path(
        '<int:refectory_id>/<int:op_type>/create',
        views.CupboardManagementCreateView.as_view(),
        name='create'
    ),

    path(
        '<int:op_type>/create',
        views.CupboardManagementCreateViewGuest.as_view(),
        name='create_guest'
    ),

    path(
        '<int:refectory_id>/<int:pk>/update',
        views.CupboardManagementUpdateView.as_view(),
        name='update'
    ),

    path(
        '<int:pk>/update',
        views.CupboardManagementUpdateViewGuest.as_view(),
        name='update_guest'
    ),

    path(
        '<int:refectory_id>/<int:pk>/delete/modal', 
        views.ModalTemplate.as_view(), 
        name='cupboard_management_modal'
        ),

    path(
        '<int:refectory_id>/<int:pk>/delete', 
        views.DeleteCupboardManagementOperation, 
        name='delete'
        ),

    path(
        '<int:refectory_id>/report',
        views.ModalTemplateReport.as_view(),
        name='cupboard_management_report_modal'
    ),

    path(
        '<int:refectory_id>/pdf',
        views.DownloadPDF.as_view(),
        name='cupboard_management_pdf'
    ),      

]