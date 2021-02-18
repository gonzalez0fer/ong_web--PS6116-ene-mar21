from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "product-managements"

urlpatterns = [
    path(
        '<int:pk>', 
        views.ProductManagementListView.as_view(), 
        name='list_product_management'
        ),
    path(
        '<int:pk>/create',
        views.ProductManagementCreateView.as_view(),
        name='create'
    )

]