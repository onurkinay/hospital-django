from django.conf import settings
from django.db import models
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

BLOOD_GROUPS = ( 
    ("1", "A Rh+"), 
    ("2", "B Rh+"), 
    ("3", "0 Rh+"), 
    ("4", "A Rh-"), 
    ("5", "B Rh-"), 
    ("6", "0 Rh-"),
    ("7","AB Rh+"),
    ("8","AB Rh-")
)

class Patient(models.Model):
    ID = models.BigAutoField(primary_key=True)
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
    DateOfBirth = models.DateField(verbose_name="Date of Birth")
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Blood_Group = models.CharField(max_length = 20,  choices = BLOOD_GROUPS, default = '1',verbose_name="Blood Group")
    Address =models.TextField()
    Phone = models.CharField(max_length=11)
    IsVisible = models.BooleanField(default=True)

    class Meta:
        db_table = "patient"
    def __str__(self):
        return str(self.User.first_name+" "+self.User.last_name)