from django.db import models


SPORT_CHOICES = (
    ('BEACH TENIS', 'Beach tennis'),
    ('VOLEI', 'Volei'),
    ('FUTVOLEI', 'Futvolei')
)
TIME_CHOICES = (
    ('17:00 - 18:00', '17:00 - 18:00'),
    ('18:00 - 19:00', '18:00 - 19:00'),
    ('19:00 - 20:00', '19:00 - 20:00'),
    ('20:00 - 21:00', '20:00 - 21:00'),
    ('21:00 - 22:00', '21:00 - 22:00'),
)


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    day = models.DateField()
    time = models.CharField(max_length=255, choices=TIME_CHOICES, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    sport = models.CharField(max_length=255, choices=SPORT_CHOICES, blank=True, null=True)
