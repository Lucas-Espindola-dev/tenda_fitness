from django.db import models


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
