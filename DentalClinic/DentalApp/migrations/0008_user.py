# Generated by Django 4.0.3 on 2022-04-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DentalApp', '0007_alter_appointment_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]