from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from .models import Application
from .forms import ApplicationForm


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
        return HttpResponseRedirect('/application/applications/')


class ApplicationPending(LoginRequiredMixin, ListView):
    context_object_name = 'pending_applications'
    queryset = Application.objects.filter()
    template_name = 'application/applications.html'


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application/update.html'
    success_url = reverse_lazy("applications")


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'application/detail.html'
    context_object_name = 'application'
    queryset = Application.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj