from django.db import models

# Create your models here.
class Bustrans(models.Model):
    Source = models.CharField(max_length=10,null=True)
    Destination = models.CharField(max_length=10,null=True)
    Bus_Number = models.CharField(max_length=10,null=True)
    Departure_Time = models.CharField(max_length=10,null=True)
    Arrival_Time = models.CharField(max_length=10,null=True)
    Distance = models.CharField(max_length=10,null=True)
    Duration = models.CharField(max_length=10,null=True)
    Number_of_Stops = models.CharField(max_length=10,null=True)

