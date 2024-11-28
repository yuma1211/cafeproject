from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


