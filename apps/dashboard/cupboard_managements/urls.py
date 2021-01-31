from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "cupboard-management"

urlpatterns = [
    path(
        '<int:pk>', 
        views.CupboardManagementListSingleView.as_view(), 
        name='list_cupboard_single_management'
        ),

    path(
        'refectory/<int:pk>', 
        views.CupboardManagementListView.as_view(), 
        name='list_cupboard_management'
        ),

]