from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    first_name = forms.CharField(required=True, widget=forms.TextInput(), label="Nome")
    last_name = forms.CharField(required=True, widget=forms.TextInput(), label="Sobrenome")
    email = forms.EmailField(required=True, widget=forms.EmailInput(), label="E-mail")
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(), label="Repita a Senha")

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail'
        }
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError('E-mail já se encontra em uso! Selecione outro!', code='invalid')

        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        message = 'As senhas não são iguais'

        if password != password2:
            raise ValidationError(
                {
                    'password': message,
                    'password2': message,
                },
            )
