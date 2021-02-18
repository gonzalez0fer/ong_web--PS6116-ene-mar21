from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "water_tanks"

urlpatterns = [
    path(
        '', 
        views.TanksListView.as_view(), 
        name='tanks_list'
        ),
    path(
        'tank/', 
        views.WaterTankSingleListView.as_view(), 
        name='tanks_list_guest'
        ),
]