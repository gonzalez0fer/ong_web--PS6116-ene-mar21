from .                      import views
from django.contrib         import admin
from django.urls            import include, path, re_path

app_name = "notifications"

urlpatterns = [
    path(
        'notifications-admin', 
        views.NotificationListView.as_view(), 
        name='notifications_list'
        ),

    path(
        'notifications', 
        views.NotificationListViewGuest.as_view(), 
        name='notifications_list_guest'
        ),
]