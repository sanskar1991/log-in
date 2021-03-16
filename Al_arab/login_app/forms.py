from django import forms
from .models import UserRegister
from django.utils.translation import gettext_lazy as _


class SignupForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = ("email", "username", "mob_number", "password")
        widgets = {
            'password': forms.PasswordInput(),
        }

class OTPVerifyForm(forms.Form):
    otp = forms.CharField(max_length=4)