from django.urls import path

from .views import HRRegistration, EmployeeAPIView, EmployeeUpdateAPIView

urlpatterns = [
    path('register/', HRRegistration.as_view(), name='register'),
    path('employee/', EmployeeAPIView.as_view(), name='emp'),
    path('employee/<pk>/', EmployeeUpdateAPIView.as_view(), name='emp'),
]