from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
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

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1"]

class PostBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ["name", "address", "image", "details", "hood"]

class AddEstablishment(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = ["name", "location", "contact", "image"]

class PostNotice(forms.ModelForm):
    class Meta:
        model = Notices
        fields = ["title", "details"]