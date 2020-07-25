import africastalking

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from .models import SMS
from .forms import SMSForm

username = settings.AFRICASTALKING_USERNAME
api_key = settings.AFRICASTALKING_API_KEY
sender = settings.AFRICASTALKING_SENDER
bulkSMSMode = 1
enqueue = 1

class SMSListView(LoginRequiredMixin, CreateView, ListView):
    context_object_name = 'messages'
    queryset = SMS.objects.filter().all()
    template_name = 'sms/sms.html'
    form_class = SMSForm

    def form_valid(self, form):
        changemaker = form.cleaned_data['changemaker']
        message = form.cleaned_data['message']

        obj = form.save(commit=False)
        obj.user = self.request.user

        africastalking.initialize(username, api_key)
        sms = africastalking.SMS

        recipients = []
        for item in changemaker:
            mobile = str(item)
            if mobile[0:2] == "07":
                mobile = mobile.replace("07", "+2547", 1)
            elif mobile[0] == "7":
                mobile = mobile.replace("7", "+2547", 1)
            elif mobile[0:4] == "2547":
                mobile = mobile.replace("2547", "+2547", 1)
            else:
                mobile = mobile
            recipients.append(mobile)
        sms.send(message, recipients)
        
        obj.save()

        return HttpResponseRedirect('/sms/')