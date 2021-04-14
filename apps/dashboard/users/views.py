from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, FormView 
from apps.main.users.models import CustomUser, UserProfile
from .forms import CustomUserForm, UserProfileForm, UserAssignRefectoryForm
from django.http import HttpResponse
from django.contrib import messages


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.main.users.decorators import superuser_required


@method_decorator([login_required, superuser_required], name='dispatch')
class UsersList(ListView):
    template_name = "users/user_list.html"
    queryset = CustomUser.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        query = CustomUser.objects.order_by('id')

        context['object_list'] = []
        for i in query:
            if not i.profile.refectory:
                refectory = '(sin asignar)'
            else:
                refectory = i.profile.refectory
            context['object_list'].append({'id':i.id,'name':i.profile.name, 
            'last_name':i.profile.last_name, 'email':i.email, 
            'is_admin':i.is_superuser, 'refectory':refectory})
        return context  

@method_decorator([login_required, superuser_required], name='dispatch')
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
        messages.success(self.request, 'Usuario actualizado exitosamente')
        return super().form_valid(form)



    def form_invalid(self, form, profile_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                profile_form=profile_form
            )
        )


class UserUpdateSingleProfile(UpdateView):
    form_class = CustomUserForm
    model = CustomUser 
    queryset = CustomUser.objects.all()
    template_name = "users/page-user.html"
    success_url = "/"

    def get_object(self):
        return CustomUser.objects.get(pk=self.request.user.id)

    def get_context_data(self, **kwargs):

        context = super(UserUpdateSingleProfile, self).get_context_data(**kwargs)

        custom_user = get_object_or_404(CustomUser, pk=self.request.user.id)

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
        messages.success(self.request, 'Usuario actualizado exitosamente')
        return super().form_valid(form)



    def form_invalid(self, form, profile_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                profile_form=profile_form
            )
        )



class UserAssignRefectory(UpdateView):
    model = UserProfile
    template_name = 'users/assign_refectory.html'
    form_class = UserAssignRefectoryForm

    def get_success_url(self, **kwargs):
        success_url = "/dashboard/user/"
        messages.success(self.request, 'Punto de distribución asignado exitosamente')
        return success_url