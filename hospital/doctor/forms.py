from django import forms
from .models import Doctor
 
 
# creating a form
class DoctorForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Doctor
 
        # specify fields to be used
        fields = [
            "DateOfBirth",
            "Gender",  
            "Phone",
            "Salary",
            "Specializations",
            "Experience",
            "Languages",
            "Department",
            "ID"
        ]