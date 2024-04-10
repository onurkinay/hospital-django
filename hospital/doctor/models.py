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
    DateOfBirth = models.DateField(verbose_name="Date of Birth")
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES,verbose_name="Gender")
    Phone = models.CharField(max_length=11,verbose_name="Phone")
    Salary = models.IntegerField(verbose_name="Salary")
    Specializations = models.CharField(max_length=300,verbose_name="Specializations")
    Experience = models.TextField(verbose_name="Experience")
    Languages = models.CharField(max_length=300,verbose_name="Languages")
    Department = models.ForeignKey(Department, on_delete=models.SET_DEFAULT,default=1,verbose_name="Department")
    IsVisible = models.BooleanField(default=True)

    class Meta:
        db_table = "doctor"
    def __str__(self):
        return str(self.User.first_name+" "+self.User.last_name + " - "+ self.Department.Name)