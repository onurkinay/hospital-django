from django import forms
from .models import Appointment
from datetime import date

class AppointmentForm(forms.ModelForm):
  
    class Meta: 
        model = Appointment
  
        fields = [
            "DoctorID", 
            "AppointmentDate", 
            "Description",
            "PatientID"
        ]

        widgets = { 
            'Description': forms.Textarea(attrs={'class': 'form-control','style':'width: 100%'}),
            'AppointmentDate': forms.DateInput(
                format=('%Y-%m-%d %H:%M:%S'),
                attrs={'class': 'form-control',  
                       'type': 'datetime-local',
                       'min': date.today().strftime("%Y-%m-%d %H:%m")
                      }),
            'PatientID': forms.HiddenInput()
        }