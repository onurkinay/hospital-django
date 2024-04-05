from django.db import models
from appointment.models import Appointment

class Bill(models.Model):
    ID = models.BigAutoField(primary_key=True)
    IssuedDate = models.DateTimeField()
    Amount = models.IntegerField()
    IsPaid = models.BooleanField()
    Appointment =  models.ForeignKey(Appointment,on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        db_table = "bill"