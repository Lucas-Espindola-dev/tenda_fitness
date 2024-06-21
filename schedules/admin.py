from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'day', 'time', 'sport',)


admin.site.register(Appointment, AppointmentAdmin)
