from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(), label='Usuário')
    password = forms.CharField(required=True, widget=forms.PasswordInput(), label='Senha')
