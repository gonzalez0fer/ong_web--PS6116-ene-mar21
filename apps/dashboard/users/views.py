from django.views.generic import ListView
from apps.main.users.models import CustomUser

class UsersList(ListView):
    template_name = "users/user_list.html"
    queryset = CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        query = CustomUser.objects.order_by('id')

        context['object_list'] = []
        for i in query:
            context['object_list'].append({'id':i.id,'name':i.profile.name, 
            'last_name':i.profile.last_name, 'email':i.email})
        return context  