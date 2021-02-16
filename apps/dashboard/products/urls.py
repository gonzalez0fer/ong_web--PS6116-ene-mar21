from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "products"

urlpatterns = [
    path(
        '<int:pk>', 
        views.ProductsListView.as_view(), 
        name='list_maintenance_product'
        ),

  

]