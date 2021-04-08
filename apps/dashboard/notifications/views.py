from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponse
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required

from apps.main.notifications.models import Notifications
from apps.main.refectories.models import Refectory
from apps.main.users.models import CustomUser

@method_decorator([login_required, superuser_required], name='dispatch')
class NotificationListView(ListView):
    model = Notifications
    template_name = ''

    def get_queryset(self):
        queryset = Notifications.objects.filter(user_notification_id=self.request.user.id)
        return queryset

class NotificationListViewGuest(ListView):
    model = Notifications
    template_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = Notifications.objects.filter(refectory_id=self.request.user.profile.refectory.id, user_notification_id=self.request.user.id)
        
        context['object_list'] = []
        for i in query:
            context['object_list'].append({
                    'id':i.id,
                    'notification_type':i.notification_type,
                    'notification_message':i.notification_message,
                    'read':i.read,
                    'created':i.created,
            })      
        return context

class NotificationCount(View):
    def get(self, request, *args, **kwargs):
        query = Notifications.objects.filter(user_notification_id=self.request.user.id,read=False)
        return len(query)

class UpdateNotificationStatus(View):
    def put(self, request, *args, **kwargs):
        notifications_list = self.request.GET.get("q")
        for i in notifications_list:
            query = Notifications.objects.get(id=i.id)
            query.read = True
            query.save()
        return 200