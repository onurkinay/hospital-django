from django import forms
from .models import Accountant
 
 
# creating a form
class AdminForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Accountant
 
        # specify fields to be used
        fields = [
            "DateOfBirth",
            "Gender",  
            "Phone",  
            "ID"
        ]