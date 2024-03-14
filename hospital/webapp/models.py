from django.db import models



# Create your models here.
#must be optimized
class Appointment(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Description = models.CharField(max_length=500)
    AppointmentDate = models.DateField()
    DoctorID = models.ForeignKey()
    PatientID = models.ForeignKey()


class Bill(models.Model):
    ID = models.BigAutoField(primary_key=True)
    IssuedDate = models.DateField()
    Amount = models.IntegerField()
    IsPaid = models.BooleanField()


class Department(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    PriceUnit =  models.IntegerField()

    

class Doctor(models.Model):
    ID = models.BigAutoField(primary_key=True)
    UserID = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Surname = models.CharField(max_length=30)
    DateOfBirth = models.DateField()
    Gender = models.BooleanField()
    Blood_Group = models.AutoField()
    Email = models.EmailField()
    Address = models.CharField(max_length=30)
    Phone = models.IntegerField()

    Salary = models.IntegerField()
    Specializations = models.CharField(max_length=30)
    Experience = models.CharField(max_length=30)
    Languages = models.CharField(max_length=30)



class Patient(models.Model):
    ID = models.BigAutoField(primary_key=True)
    UserID = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Surname = models.CharField(max_length=30)
    DateOfBirth = models.DateField()
    Gender = models.BooleanField()
    Blood_Group = models.AutoField()
    Email = models.EmailField()
    Address = models.CharField(max_length=30)
    Phone = models.IntegerField()

class Prescription(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Medicinde = models.CharField(max_length=30)
    Remark = models.CharField(max_length=30)
    Advice = models.CharField(max_length=30)
    Appointment_ID = models.ForeignKey()

