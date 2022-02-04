from unittest.util import _MAX_LENGTH
from argon2 import PasswordHasher
from click import password_option
from django import forms
from django.forms import ModelForm
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = 'username', 'password'



