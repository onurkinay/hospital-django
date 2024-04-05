from django import forms
from .models import Prescription
 
  
class PrescriptionForm(forms.ModelForm):
  
    class Meta: 
        model = Prescription
  
        fields = [
            "Medicinde",
            "Remark",
            "Advice",
            "Appointment"
        ] 
        
        widgets = { 
            
        }