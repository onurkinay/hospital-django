# Generated by Django 5.0.3 on 2024-04-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='AppointmentDate',
            field=models.DateTimeField(),
        ),
    ]
