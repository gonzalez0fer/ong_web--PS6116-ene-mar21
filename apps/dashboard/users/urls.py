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

    path(
        'profile/', 
        views.UserUpdateSingleProfile.as_view(), 
        name='edit_profile'
        ),

    path(
        'assign/<int:pk>', 
        views.UserAssignRefectory.as_view(), 
        name='assign_refectory'
        ),

]