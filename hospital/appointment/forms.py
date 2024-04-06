from django import forms
from .models import Appointment
 
#Giriş yapan hastanın IDsi varsayılan olarak seçilmeli ve değiştirilmesine izin verilmemeli

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
                       'placeholder': 'Select a date',
                       'type': 'datetime-local'  
                      }),
            'PatientID': forms.HiddenInput(attrs={'value':'1'})
        }