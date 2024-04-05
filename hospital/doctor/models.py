from django.conf import settings
from django.db import models
from department.models import Department

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class Doctor(models.Model):
    ID = models.BigAutoField(primary_key=True)
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Phone = models.CharField(max_length=11)
    Salary = models.IntegerField()
    Specializations = models.CharField(max_length=300)
    Experience = models.TextField()
    Languages = models.CharField(max_length=300)
    Department = models.ForeignKey(Department, on_delete=models.SET_DEFAULT,default=1)

    class Meta:
        db_table = "doctor"