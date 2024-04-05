from django.db import models

class Department(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    PriceUnit =  models.IntegerField()

    class Meta:
        db_table = "department"
    def __str__(self):
        return str(self.Name)