from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth import get_user_model
from .models import UserRegister

User = get_user_model()

class SignupForm(forms.ModelForm):
    
    class Meta:
        model = UserRegister
        fields = ("email", "username", "mob_number", "password")
        widgets = {
            'password': forms.PasswordInput(),
        }