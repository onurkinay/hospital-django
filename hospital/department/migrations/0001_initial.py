# Generated by Django 5.0.3 on 2024-04-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('PriceUnit', models.IntegerField()),
            ],
        ),
    ]