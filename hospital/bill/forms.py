from django import forms
from .models import Bill
 
  
class BillForm(forms.ModelForm):
  
    class Meta: 
        model = Bill
  
        fields = [
            "IssuedDate",
            "Amount",
            "IsPaid"
        ]

        
        widgets = { 
           
            'IssuedDate': forms.DateInput(
                format=('%Y-%m-%d %H:%M:%S'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'datetime-local'  
                      }),
        }