from django.urls import path
from schedules.views import AppointmentCreateListView, AppoitmentRetrieveUpdateDestroyView, UserAppointmentsView, AvailibleSlotsView


urlpatterns = [
    path('appointment/', AppointmentCreateListView.as_view(), name='appointment-create-list'),
    path('appointment/<int:pk>/', AppoitmentRetrieveUpdateDestroyView.as_view(), name='appointment-detail-view'),
    path('users/<str:username>/bookings/', UserAppointmentsView.as_view(), name='user-bookings'),
    path('availible-slots/', AvailibleSlotsView.as_view(), name='availible-slots'),
]