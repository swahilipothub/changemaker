# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, Profile

@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('mobile_number', 'is_staff', 'is_active',)
    list_filter = ('mobile_number', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('mobile_number', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile_number', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('mobile_number',)
    ordering = ('mobile_number',)


admin.site.register(Profile)
