from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "refectory"

urlpatterns = [
    path(
        '', 
        views.RefectoriesListView.as_view(), 
        name='list_refectories'
        ),

    path(
        'create/', 
        views.RefectoryCreateView.as_view(), 
        name='create_refectory'
        ),

    path(
        '<int:pk>', 
        views.RefectoryUpdateView.as_view(), 
        name='edit_refectory'
        ),

]