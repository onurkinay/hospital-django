from django import forms
from .models import Department
 
 
# creating a form
class DepartmentForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Department
 
        # specify fields to be used
        fields = [
            "Name",
            "PriceUnit",
        ]