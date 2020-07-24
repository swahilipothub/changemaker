# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import template

from users.models import User, Profile
from application.models import Application
from application.forms import ApplicationForm

@login_required(login_url="/login/")
def index(request):
    users = Profile.objects.all()
    total_users = Profile.objects.count()
    total_applications = Application.objects.count()
    pending_applications = Application.objects.filter(status="PENDING").count()

    return render(
        request, "index.html", 
        {
            "users": users, 
            "total_users": total_users, 
            "total_applications": total_applications,
            "pending_applications": pending_applications
        })


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'
    context_object_name = 'profile'
    queryset = Profile.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj


class Apply(CreateView):
    template_name = 'application/apply.html'
    form_class = ApplicationForm
    # success_url = reverse_lazy("/login/")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        print("hdsjdhhhhhhhhhhhhhhhhhhh")
        return HttpResponseRedirect('/login/')


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
