from rest_framework import serializers
from schedules.models import Appointment


class AppointmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
