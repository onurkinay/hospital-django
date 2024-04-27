
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('home.urls')), 
    path('Patients/',include('patient.urls')),
    path('Doctors/',include('doctor.urls')),
    path('Prescriptions/',include('prescription.urls')),
    path('Departments/',include('department.urls')),
    path('Bills/',include('bill.urls')),
    path('Appointments/',include('appointment.urls')),
    path('Admins/',include('administrator.urls')),
    path('Accountants/',include('accountant.urls')),
]
