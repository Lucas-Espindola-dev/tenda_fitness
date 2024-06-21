from django.db import models
from django.contrib.auth.models import User


SPORT_CHOICES = (
    ('BEACH TENNIS', 'Beach tennis'),
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    day = models.DateField()
    time = models.CharField(max_length=255, choices=TIME_CHOICES, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    sport = models.CharField(max_length=255, choices=SPORT_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
