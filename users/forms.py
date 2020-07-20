# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, Profile


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('mobile_number',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('mobile_number',)


class LoginForm(forms.Form):
    mobile_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Mobile Number",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    mobile_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Mobile Number",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('mobile_number', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Location",                
                "class": "form-control"
            }
        ))
    birth_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Birth Date",                
                "class": "form-control"
            }
        ))
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Bio",                
                "class": "form-control",
                "rows": 4,
                'style': 'height: 6em;'
            }
        ))
    
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'location', 'birth_date', 'bio',)

    def save(self, *args, **kwargs):
        u = self.instance
        u.save()
        profile = super(ProfileForm, self).save(*args, **kwargs)
        return profile