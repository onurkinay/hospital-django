# Generated by Django 5.0.3 on 2024-04-05 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_doctor_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='Blood_Group',
        ),
    ]