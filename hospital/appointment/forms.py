from django import forms
from .models import Appointment
 
 
# creating a form
class AppointmentForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Appointment
 
        # specify fields to be used
        fields = [
            "Description",
            "AppointmentDate",
            "DoctorID"
        ]