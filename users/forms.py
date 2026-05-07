from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class CreateUserForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'role',
            'password'
        ]