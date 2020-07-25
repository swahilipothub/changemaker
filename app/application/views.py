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
        return HttpResponseRedirect("applications")


class ApplicationPending(LoginRequiredMixin, ListView):
    context_object_name = 'pending_applications'
    queryset = Application.objects.filter()
    template_name = 'application/applications.html'


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application/update.html'

    def form_valid(self, form):
        africastalking.initialize(username, api_key)
        sms = africastalking.SMS
        
        status = form.cleaned_data['status']
        mobile_number = form.cleaned_data['mobile_number']

        recipients = str(mobile_number)
        if recipients[0:2] == "07":
            recipients = recipients.replace("07", "+2547", 1)
        elif recipients[0] == "7":
            recipients = recipients.replace("7", "+2547", 1)
        elif recipients[0:4] == "2547":
            recipients = recipients.replace("2547", "+2547", 1)
        else:
            recipients = recipients
        
        message = "Hi, you application has been approved!"
        print(message, recipients)

        if status == 'PENDING':
            print("Yeeeeeeeeeeeeeeeeeeeeee")
            sms.send(message, recipients)
        
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect('/application/')


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'application/detail.html'
    context_object_name = 'application'
    queryset = Application.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj