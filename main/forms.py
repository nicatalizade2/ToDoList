from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from main.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['image', 'title', 'description', 'complete']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
