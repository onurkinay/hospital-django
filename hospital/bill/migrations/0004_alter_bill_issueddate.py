# Generated by Django 5.0.3 on 2024-04-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0003_bill_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='IssuedDate',
            field=models.DateTimeField(),
        ),
    ]
