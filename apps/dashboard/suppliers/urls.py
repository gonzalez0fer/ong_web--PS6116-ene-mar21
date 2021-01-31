from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "supplier"

urlpatterns = [
    path(
        '', 
        views.SuppliersListView.as_view(), 
        name='list_suppliers'
        ),

    path(
        'create/', 
        views.SupplierCreateView.as_view(), 
        name='create_supplier'
        ),

    path(
        '<int:pk>', 
        views.SupplierUpdateView.as_view(), 
        name='edit_supplier'
        ),
]