# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
# from .views import login_view, register_user, ProfileView
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/settings/', views.settings, name='settings'),
    # path('profile/change_password/', views.change_password, name='change_password'),
]
