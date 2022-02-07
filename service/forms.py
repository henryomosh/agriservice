from django import forms
from django.contrib.auth.forms import UserCreationForm, ValidationError
from .models import *


class SignupForm(UserCreationForm):
    name = forms.CharField(required=False, )
    email = forms.CharField(required=True)
    password1 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('The given email is already registered')
        return self.cleaned_data['email']