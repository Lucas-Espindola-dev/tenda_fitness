from rest_framework import generics
from django.views.generic import ListView, CreateView
from django.shortcuts import render
from schedules.models import Appointment
from .forms import AppointmentForm
from schedules.serializers import AppointmentModelSerializer, UserAppointmentsSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def home(request):
    return render(request, 'schedules/home.html')


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'schedules/appointments_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.all().order_by('day')


@method_decorator(login_required(login_url='login'), name='dispatch')
class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'schedules/new_appointment.html'
    success_url = '/appointments/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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


class UserAppointmentsAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAppointmentsSerializer
    lookup_field = 'username'
