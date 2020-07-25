import africastalking

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from .models import Application
from .forms import ApplicationForm

from users.models import User, Profile

username = settings.AFRICASTALKING_USERNAME
api_key = settings.AFRICASTALKING_API_KEY
sender = settings.AFRICASTALKING_SENDER
bulkSMSMode = 1
enqueue = 1

class ApplicationListView(LoginRequiredMixin, CreateView, ListView):
    context_object_name = 'applications'
    queryset = Application.objects.all()
    template_name = 'application/applications.html'
    form_class = ApplicationForm
    model = Application
    paginate_by = 10

    def form_valid(self, form):
        obj = form.save(commit=False)
        # obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect("/application/")


class ApplicationPending(LoginRequiredMixin, ListView):
    context_object_name = 'pending_applications'
    queryset = Application.objects.filter()
    template_name = 'application/applications.html'


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application/update.html'

    def form_valid(self, form):
        obj = form.save(commit=False)

        africastalking.initialize(username, api_key)
        sms = africastalking.SMS

        status = form.cleaned_data['status']
        mobile_number = form.cleaned_data['mobile_number']
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        birth_date = form.cleaned_data['birth_date']
        location = form.cleaned_data['subcounty']
        password = User.objects.make_random_password()

        to = []
        recipients = mobile_number
        if recipients[0:2] == "07":
            recipients = recipients.replace("07", "+2547", 1)
        elif recipients[0] == "7":
            recipients = recipients.replace("7", "+2547", 1)
        elif recipients[0:4] == "2547":
            recipients = recipients.replace("2547", "+2547", 1)
        else:
            recipients = recipients
        to.append(recipients)

        message = ""
        if status == 'APPROVED':
            message = """Hi %s, your application has been approved! Use your mobile number: %s and password: %s to login to the portal""" % (first_name, mobile_number, password) 
            if User.objects.filter(mobile_number=mobile_number).exists():
                print(u'User with this mobile number "%s" is already in use.' % mobile_number)
                obj.user = User.objects.get(mobile_number=mobile_number)
            else:
                user = User.objects.create(mobile_number=mobile_number, password=password)
                profile = Profile.objects.get(user=user)
                profile.email = email
                profile.first_name = first_name
                profile.last_name = last_name
                profile.birth_date = birth_date
                profile.location = location
                profile.save()
                print("New Password", password, "User:", user)
                obj.user = user
        elif status == 'CNACELLED':
            message = """Hi %s, your application has been declined. Please send us an email if you have further questions changemaker@swahilipothub.co.ke""" % (first_name,)
        
        sms.send(message, to)
        obj.save()
        return HttpResponseRedirect('/application/')


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'application/detail.html'
    context_object_name = 'application'
    queryset = Application.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj