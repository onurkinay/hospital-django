
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('',include('home.urls')), 
    path('patient/',include('patient.urls')),
    path('doctor/',include('doctor.urls')),
    path('prescription/',include('prescription.urls')),
    path('department/',include('department.urls')),
    path('bill/',include('bill.urls')),
    path('appointment/',include('appointment.urls')),
]
