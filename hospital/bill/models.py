from django.db import models

class Bill(models.Model):
    ID = models.BigAutoField(primary_key=True)
    IssuedDate = models.DateField()
    Amount = models.IntegerField()
    IsPaid = models.BooleanField()

    class Meta:
        db_table = "bill"