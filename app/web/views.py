# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
    cancelled_applications = Application.objects.filter(status="CANCELLED").count()
    approved_applications = Application.objects.filter(status="APPROVED").count()

    return render(
        request, "index.html", 
        {
            "users": users, 
            "total_users": total_users, 
            "total_applications": total_applications,
            "pending_applications": pending_applications,
            "cancelled_applications": cancelled_applications,
            "approved_applications": approved_applications,
        })

def get_gender_data(request, *args, **kwargs):
    labels = ["Male", "Female"]
    male = Profile.objects.filter(gender='Male').count()
    female = Profile.objects.filter(gender='Female').count()
    default_data = [male, female]
    
    data = {
        "labels": labels,
        "default_data": default_data
    }
    return JsonResponse(data)

def get_subcounty_data(request, *args, **kwargs):
    subcounty_labels = ["Mvita", "Kisauni", "Nyali", "Changamwe", "Jomvu", "Likoni"]
    mvita = Application.objects.filter(subcounty="Mvita").count()
    kisauni = Application.objects.filter(subcounty="Kisauni").count()
    nyali = Application.objects.filter(subcounty="Nyali").count()
    changamwe = Application.objects.filter(subcounty="Changamwe").count()
    jomvu = Application.objects.filter(subcounty="Jomvu").count()
    likoni = Application.objects.filter(subcounty="likoni").count()
    subcounty_data = [mvita, kisauni, nyali, changamwe, jomvu, likoni]

    data = {
        "subcounty_labels": subcounty_labels,
        "subcounty_data": subcounty_data
    }
    return JsonResponse(data)

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
