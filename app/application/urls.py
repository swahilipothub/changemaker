from django.urls import path
from .views import ApplicationListView, ApplicationDetailView, ApplicationPending, ApplicationUpdateView

urlpatterns = [
    path('', ApplicationListView.as_view(), name='applications'),
    path('', ApplicationPending.as_view(), name='applications-pending'),
    path('<int:pk>', ApplicationDetailView.as_view(), name='application-detail'),
    path('update/<int:pk>', ApplicationUpdateView.as_view(), name='application-update'),
    # path('apply/', ApplicationCreateView.as_view(), name='application-add'),
]