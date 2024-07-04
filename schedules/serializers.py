from rest_framework import serializers
from schedules.models import Appointment
from django.contrib.auth.models import User
from datetime import datetime


class AppointmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = instance.user.username
        return rep


class UserAppointmentsSerializer(serializers.ModelSerializer):
    booked_slots = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'booked_slots']

    def get_booked_slots(self, obj):
        today = datetime.today().date()
        return Appointment.objects.filter(user=obj, day__gte=today).values('day', 'time')


class AvailiableSlotsSerializer(serializers.ModelSerializer):
    availible_slots = serializers.SerializerMethodField()

    def get_availible_slots(self, obj):
        booked_slots = Appointment.objects.filter(day=obj['day']).values_list('time', flat=True)
        all_slots = [f'{hour}:00' for hour in range(17, 22)]
        availible_slots = [slot for slot in all_slots if slot not in booked_slots]
        return availible_slots
