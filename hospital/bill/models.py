from django.db import models
from appointment.models import Appointment

class Bill(models.Model):
    ID = models.BigAutoField(primary_key=True)
    IssuedDate = models.DateTimeField(verbose_name="Issued Date")
    Amount = models.IntegerField(verbose_name="Amount")
    IsPaid = models.BooleanField(verbose_name="Is Paid?")
    Appointment =  models.ForeignKey(Appointment,on_delete=models.CASCADE,blank=True, null=True,verbose_name="Appointment")

    class Meta:
        db_table = "bill"