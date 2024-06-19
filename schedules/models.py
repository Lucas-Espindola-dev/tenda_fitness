from django.db import models


SPORT_CHOICES = (
    ('BEACH TENIS', 'Beach tennis'),
    ('VOLEI', 'Volei'),
    ('FUTVOLEI', 'Futvolei')
)

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date_appointment = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    time = models.TimeField()
    sport = models.CharField(max_length=255, choices=SPORT_CHOICES, blank=True, null=True)
