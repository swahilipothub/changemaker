from django.urls import path
from .views import SMSListView

urlpatterns = [
    path('', SMSListView.as_view(), name='sms'),
]