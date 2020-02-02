from django.urls import path
from .views import *
urlpatterns = [
    path('employee_api/', EmployeeAPI.as_view()),
    path('employee_api/<int:id>/', EmployeeDetailView.as_view()),
]
