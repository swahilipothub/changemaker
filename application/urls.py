from django.urls import path
from .views import ApplicationListView, ApplicationCreateView, ApplicationDetailView, ApplicationPending

urlpatterns = [
    path('', ApplicationListView.as_view(), name='applications'),
    path('', ApplicationPending.as_view(), name='applications-pending'),
    path('<int:pk>', ApplicationDetailView.as_view(), name='application-detail'),
    path('apply/', ApplicationCreateView.as_view(), name='application-add'),
]