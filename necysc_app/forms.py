from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email', max_length=255)
    
    class Meta:
        model = User
        fields = ['email', 'password']

