from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "cupboard"

urlpatterns = [
    path(
        '<int:pk>', 
        views.CupboardsListView.as_view(), 
        name='list_cupboard'
        ),

    path(
        'products/', 
        views.CupboardsSingleListView.as_view(), 
        name='list_products'
        ),

]