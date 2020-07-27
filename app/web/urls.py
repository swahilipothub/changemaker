# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from web import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('api/data/gender/', views.get_gender_data, name='api-data-gender'),
    path('api/data/subcounty/', views.get_subcounty_data, name='api-data-subcounty'),
    path('apply/', views.Apply.as_view(), name='apply'),
    # path('<int:pk>', views.ProfileDetailView.as_view(), name='profile-detail'),
]
