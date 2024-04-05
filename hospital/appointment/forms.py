from django import forms
from .models import Appointment
 
  
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
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }