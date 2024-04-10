# Generated by Django 5.0.3 on 2024-04-10 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_appointment_isvisible_and_more'),
        ('bill', '0004_alter_bill_issueddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Amount',
            field=models.IntegerField(verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='Appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appointment.appointment', verbose_name='Appointment'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='IsPaid',
            field=models.BooleanField(verbose_name='Is Paid?'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='IssuedDate',
            field=models.DateTimeField(verbose_name='Issued Date'),
        ),
    ]