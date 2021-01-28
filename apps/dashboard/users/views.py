from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView 
from extra_views import UpdateWithInlinesView
from apps.main.users.models import CustomUser, UserProfile
from .forms import CustomUserForm, UserProfileForm
from django.http import HttpResponse



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
            'last_name':i.profile.last_name, 'email':i.email, 'is_admin':i.is_superuser})
        return context  

class UserUpdateProfile(UpdateView):
    form_class = CustomUserForm
    model = CustomUser 
    queryset = CustomUser.objects.all()
    template_name = "users/page-user.html"
    success_url = "/dashboard/user/"

    def get_context_data(self, **kwargs):

        context = super(UserUpdateProfile, self).get_context_data(**kwargs)

        custom_user = get_object_or_404(CustomUser, pk=self.kwargs['pk'])

        try:
            user_profile = custom_user.profile
        except:
            user_profile = None

        if 'profile_form' not in context:
            
            context['profile_form'] = UserProfileForm(
                instance = user_profile,
                initial = {
                    'name':user_profile.name,
                    'last_name':user_profile.last_name,
                    'address':user_profile.address,
                    'about':user_profile.about,
                }
            )
        return context
    
    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()

        profile_form = UserProfileForm(
            request.POST,
            instance = self.object.profile
        )

        if form.is_valid() and profile_form.is_valid():
            print('LO LOG')
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        self.object = form.save(commit=False)
        self.object.profile.name = profile_form.cleaned_data['name']
        self.object.profile.last_name = profile_form.cleaned_data['last_name']
        self.object.profile.address = profile_form.cleaned_data['address']
        self.object.profile.about = profile_form.cleaned_data['about']
        self.object.profile.save()
        return super().form_valid(form)



    def form_invalid(self, form, profile_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                profile_form=profile_form
            )
        )