from django.urls import path
from .views import SMSListView, SMSTemplateView, ATSettingsView

urlpatterns = [
    path('', SMSListView.as_view(), name='sms'),
    path('settings/', ATSettingsView.as_view(), name='sms-settings'),
    path('templates/', SMSTemplateView.as_view(), name='sms-templates'),
]