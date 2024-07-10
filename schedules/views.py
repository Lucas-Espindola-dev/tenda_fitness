from rest_framework import generics
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse
from django.shortcuts import render, redirect
from schedules.models import Appointment
from .forms import AppointmentForm
from schedules.serializers import AppointmentModelSerializer, AvailiableSlotsSerializer, UserAppointmentsSerializer
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'schedules/appointments_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.all().order_by('day')


class AppointmentCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'schedules/new_appointment.html'

    def get(self, request, *args, **kwargs):
        day = request.GET.get('day')
        availible_slots = []

        if day:
            try:
                day = datetime.strptime(day, 'Y%-m%-d%').date()
                booked_slots = Appointment.objects.filter(day=day).values_list('time', flat=True)
                all_slots = [f'{hour:02}:00' for hour in range(17, 22)]
                availible_slots = [slot for slot in all_slots if slot not in booked_slots]
            except ValueError:
                availible_slots = []

        return render(request, self.template_name, {'availible_slots': availible_slots})

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointments-list')
        return render(request, self.template_name, {'form': form})


class UserAppointmentsListView(ListView):
    model = Appointment
    template_name = 'schedules/user_appointments_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return Appointment.objects.filter(user).order_by('-date')


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
