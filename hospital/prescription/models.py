from django.db import models
from appointment.models import Appointment

class Prescription(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Medicinde = models.CharField(max_length=30)
    Remark = models.TextField()
    Advice = models.TextField()
    Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    class Meta:
        db_table = "prescription"
