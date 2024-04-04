# Generated by Django 5.0.3 on 2024-04-04 12:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('DateOfBirth', models.DateField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Blood_Group', models.CharField(choices=[('1', 'A Rh+'), ('2', 'B Rh+'), ('3', '0 Rh+'), ('4', 'A Rh-'), ('5', 'B Rh-'), ('6', '0 Rh-')], default='1', max_length=1)),
                ('Address', models.TextField()),
                ('Phone', models.CharField(max_length=11)),
                ('Salary', models.IntegerField()),
                ('Specializations', models.CharField(max_length=300)),
                ('Experience', models.TextField()),
                ('Languages', models.CharField(max_length=300)),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
