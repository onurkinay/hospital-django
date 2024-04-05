from django import forms
from .models import Patient
 
 
# creating a form
class PatientForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Patient
 
        # specify fields to be used
        fields = [ 
            "DateOfBirth",  
            "Gender",
            "Blood_Group",
            "Address",
            "Phone"
        ]