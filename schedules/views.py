from rest_framework import generics
from schedules.models import Appointment
from schedules.serializers import AppointmentModelSerializer, AvailiableSlotsSerializer
from datetime import datetime


class AppointmentCreateListView(generics.ListCreateAPIView):
    serializer_class = AppointmentModelSerializer
    queryset = Appointment.objects.all()


class AppoitmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentModelSerializer
    queryset = Appointment.objects.all()


class AvailibleSlotsView(generics.ListAPIView):
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

