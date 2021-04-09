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
        'notifications-user', 
        views.NotificationListViewGuest.as_view(), 
        name='notifications_list_guest'
        ),

    path(
        'notifications-count', 
        views.NotificationCount.as_view(), 
        name='notifications_count'
        ),

    path(
        '<int:pk>/notifications-read-update', 
        views.UpdateNotificationRead.as_view(), 
        name='notifications_read_update'
        ),

    path(
        '<int:pk>/notifications-status-update', 
        views.UpdateNotificationStatus.as_view(), 
        name='notifications_status_update'
        ),
]