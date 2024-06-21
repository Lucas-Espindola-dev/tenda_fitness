from rest_framework import generics
from schedules.models import Appointment
from schedules.serializers import AppointmentModelSerializer
import datetime


class AppointmentCreateListView(generics.ListCreateAPIView):
    serializer_class = AppointmentModelSerializer
    queryset = Appointment.objects.all()


class AppoitmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentModelSerializer
    queryset = Appointment.objects.all()


