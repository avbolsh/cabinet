from django.urls import path
from .views import EmployeeAPIView, EmployeeDetailView

urlpatterns = [
        path('employees/', EmployeeAPIView.as_view(), name="employees"),
        path('employees/<str:uid>/', EmployeeDetailView.as_view(), name="employee-detail"),
        ]
