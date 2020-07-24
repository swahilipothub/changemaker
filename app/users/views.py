# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.forms.utils import ErrorList
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignUpForm, ProfileForm
from .models import User, Profile


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            mobile_number = form.cleaned_data.get("mobile_number")
            password = form.cleaned_data.get("password")
            user = authenticate(mobile_number=mobile_number, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            mobile_number = form.cleaned_data.get("mobile_number")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(mobile_number=mobile_number, password=raw_password)

            msg     = 'User created.'
            success = True
            
            return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })


@login_required
def settings(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    form = ProfileForm(instance=profile)
    form_pwd = PasswordChangeForm(request.user, request.POST)
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        form_pwd = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated the Profile Successfully!")
            return HttpResponseRedirect('/profile/settings/')

        elif form_pwd.is_valid():
            user = form_pwd.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('/profile/settings/'))

    return render(request, 'accounts/settings.html', {
        'form': form,
        'form_pwd': form_pwd,
        'profile': profile
    })


# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, 'Your password was successfully updated!')
#             return HttpResponseRedirect(reverse('profile'))
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'accounts/change_password.html', {
#         'form': form
#     })
