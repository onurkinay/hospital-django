# Generated by Django 5.0.3 on 2024-04-05 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0002_alter_prescription_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='Appointment_ID',
            new_name='Appointment',
        ),
    ]