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
        '<int:refectory_id>/create',
        views.ProductManagementCreateView.as_view(),
        name='create'
    ),
    path(
        '<int:refectory_id>/<int:pk>/update',
        views.ProductManagementUpdateView.as_view(),
        name='update'
    )
    

]