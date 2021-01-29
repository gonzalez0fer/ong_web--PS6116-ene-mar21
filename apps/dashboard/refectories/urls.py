from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "refectory"

urlpatterns = [
    path(
        '', 
        views.RefectoriesList.as_view(), 
        name='list_refectories'
        ),

]