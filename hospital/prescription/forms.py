from django import forms
from .models import Prescription
 
  
class PrescriptionForm(forms.ModelForm):
  
    class Meta: 
        model = Prescription
  
        fields = [
            
            "Appointment", 
            "Medicinde",
            "Remark",
            "Advice"
        ] 
        
        widgets = { 
            
        }