from rest_framework import generics
from schedules.models import Appointment
from schedules.serializers import AppointmentModelSerializer, AvailiableSlotsSerializer, UserAppointmentsSerializer
from django.contrib.auth.models import User
from datetime import datetime


class AppointmentCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = AppointmentModelSerializer
    queryset = Appointment.objects.all()


class AppoitmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentModelSerializer
    queryset = Appointment.objects.all()


class AvailibleSlotsAPIView(generics.ListAPIView):
    serializer_class = AvailiableSlotsSerializer

    def get_queryset(self):
        day = self.request.query_params.get('day')
        if day:
            try:
                day = datetime.strptime(day, '%Y-%m-%d').date()
                return [{'day': day}]
            except ValueError:
                return []
        return []


class UserAppointmentsAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAppointmentsSerializer
    lookup_field = 'username'
