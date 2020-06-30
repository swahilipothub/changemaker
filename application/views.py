from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from .models import Application
from .forms import ApplicationForm


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    # model = Application
    form_class = ApplicationForm
    template_name = 'application/create.html'
    success_url = reverse_lazy('applications')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect('/application/')


class ApplicationListView(LoginRequiredMixin, ListView):
    context_object_name = 'applications'
    queryset = Application.objects.all()
    template_name = 'application/list.html'


class ApplicationPending(LoginRequiredMixin, ListView):
    context_object_name = 'pending_applications'
    queryset = Application.objects.all()
    template_name = 'application/list.html'


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'application/detail.html'
    context_object_name = 'application'
    queryset = Application.objects.all()

    def get_object(self):
        obj = super().get_object()
        # obj.last_accessed = timezone.now()
        # obj.save()
        return obj