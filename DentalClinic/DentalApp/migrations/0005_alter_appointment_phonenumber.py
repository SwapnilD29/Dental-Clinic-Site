# Generated by Django 4.0.3 on 2022-04-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DentalApp', '0004_alter_appointment_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phoneNumber',
            field=models.CharField(max_length=12),
        ),
    ]
