from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "user"

urlpatterns = [
    path(
        '', 
        views.UsersList.as_view(), 
        name='list_users'
        ),

    path(
        '<int:pk>', 
        views.UserUpdateProfile.as_view(), 
        name='edit_user'
        ),

]