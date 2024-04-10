from django.db import models
from doctor.models import Doctor
from patient.models import Patient


class Appointment(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Description = models.TextField(verbose_name="Description")
    AppointmentDate = models.DateTimeField(verbose_name="Appointment Date")
    DoctorID = models.ForeignKey(Doctor,on_delete=models.PROTECT,verbose_name="Doctor")
    PatientID = models.ForeignKey(Patient,on_delete=models.PROTECT, verbose_name="Patient")
    IsVisible = models.BooleanField(default=True)

    class Meta:
        db_table = "appointment"
    def __str__(self):
        return str(str(self.AppointmentDate) + " "+ self.DoctorID.User.first_name)
