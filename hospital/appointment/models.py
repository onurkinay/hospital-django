from django.db import models
from doctor.models import Doctor
from patient.models import Patient


class Appointment(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Description = models.TextField()
    AppointmentDate = models.DateTimeField()
    DoctorID = models.ForeignKey(Doctor,on_delete=models.PROTECT)
    PatientID = models.ForeignKey(Patient,on_delete=models.PROTECT)

    class Meta:
        db_table = "appointment"
    def __str__(self):
        return str(str(self.AppointmentDate) + " "+ self.DoctorID.User.first_name)
