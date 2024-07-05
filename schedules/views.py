from rest_framework import generics
from django.views.generic import ListView, CreateView
from django.urls import reverse
from schedules.models import Appointment
from .forms import AppointmentForm
from schedules.serializers import AppointmentModelSerializer, AvailiableSlotsSerializer, UserAppointmentsSerializer
from django.contrib.auth.models import User
from datetime import datetime


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'schedules/appointments_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.all().order_by('day')


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'schedules/new_appointment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('appointments-list')


class UserAppointmentsListView(ListView):
    model = Appointment
    template_name = ...
    context_object_name = 'appointments'

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return Appointment.objects.filter(user).order_by('-date')


class AvailibleSlotsListView(ListView):
    template_name = ...
    context_object_name = 'availible_slots'

    def get_queryset(self):
        day = self.request.GET.get('day')
        if day:
            try:
                day = datetime.strptime(day, '%Y-%m-%d').date()
                booked_slots = Appointment.objects.filter(day=day).values_list('time', flat=True)
                all_slots = [f'{hour}:00' for hour in range(17, 22)]
                availible_slots = [slot for slot in all_slots if slot not in booked_slots]
                return availible_slots
            except ValueError:
                return []
        return []


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
