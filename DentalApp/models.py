from django.db import models


# Create your models here.
class Appointment(models.Model):
    fullName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    service = models.CharField(max_length=25)
    date = models.DateField(null=False, blank = False)
    time = models.TimeField(null=False, blank = False)
    

