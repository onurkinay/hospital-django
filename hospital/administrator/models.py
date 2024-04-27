from django.db import models

from django.conf import settings
from django.db import models 

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class Administrator(models.Model):
    ID = models.BigAutoField(primary_key=True)
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
    DateOfBirth = models.DateField(verbose_name="Date of Birth")
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES,verbose_name="Gender")
    Phone = models.CharField(max_length=11,verbose_name="Phone")
    IsVisible = models.BooleanField(default=True)

    class Meta:
        db_table = "administrator"
    def __str__(self):
        return str("Admin: "+self.User.first_name+" "+self.User.last_name)
