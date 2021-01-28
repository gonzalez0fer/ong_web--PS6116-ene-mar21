from django import forms
from django.contrib.auth import get_user_model
from apps.main.users.models import UserProfile, CustomUser
from extra_views import InlineFormSet

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email',]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [            
                'name',
                'last_name',
                'address',
                'about',
                ]
        


