from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["contacts", "image", "bio", "hood"]