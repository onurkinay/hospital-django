from django.conf import settings
from django.db import models

BLOOD_GROUPS = ( 
    ("1", "A Rh+"), 
    ("2", "B Rh+"), 
    ("3", "0 Rh+"), 
    ("4", "A Rh-"), 
    ("5", "B Rh-"), 
    ("6", "0 Rh-")
)

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class Doctor(models.Model):
    ID = models.BigAutoField(primary_key=True)
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Blood_Group = models.CharField(max_length = 1,  choices = BLOOD_GROUPS, default = '1')
    Address = models.TextField()
    Phone = models.CharField(max_length=11)
    Salary = models.IntegerField()
    Specializations = models.CharField(max_length=300)
    Experience = models.TextField()
    Languages = models.CharField(max_length=300)

    class Meta:
        db_table = "doctor"