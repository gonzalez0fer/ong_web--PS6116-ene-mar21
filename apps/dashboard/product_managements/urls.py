from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "product-managements"

urlpatterns = [
    path(
        '<int:refectory_id>', 
        views.ProductManagementListView.as_view(), 
        name='list_product_management'
        ),

    path(
        'operations', 
        views.ProductManagementListViewGuest.as_view(), 
        name='list_product_management_guest'
        ),

    path(
        '<int:refectory_id>/<int:op_type>/create',
        views.ProductManagementCreateView.as_view(),
        name='create'
    ),

    path(
        '<int:op_type>/create',
        views.ProductManagementCreateViewGuest.as_view(),
        name='create_guest'
    ),

    path(
        '<int:refectory_id>/<int:pk>/update',
        views.ProductManagementUpdateView.as_view(),
        name='update'
    ),

    path(
        '<int:pk>/update',
        views.ProductManagementUpdateViewGuest.as_view(),
        name='update_guest'
    ),

    path(
        '<int:refectory_id>/<int:pk>/delete/modal', 
        views.ModalTemplate.as_view(), 
        name='product_management_modal'
        ),

    path(
        '<int:refectory_id>/<int:pk>/delete', 
        views.DeleteProductManagementOperation, 
        name='delete'
        ),      
    

]