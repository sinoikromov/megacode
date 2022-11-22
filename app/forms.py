from .models import Client
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'second_name',  'patronymic', 'age', 'gender', 'was_born', 'email',
                  'phone',  'passport_left', 'passport_right', 'recipient_amonatbonck')


class AdminClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'second_name',  'patronymic', 'age', 'gender', 'was_born', 'email', 'status_document',
                  'passport_left', 'passport_right', 'recipient_amonatbonck', 'phone', 'editable', 'is_active')
