# Generated by Django 4.0.3 on 2022-04-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DentalApp', '0003_alter_appointment_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phoneNumber',
            field=models.IntegerField(),
        ),
    ]