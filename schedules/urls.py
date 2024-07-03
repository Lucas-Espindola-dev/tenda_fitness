from django.urls import path
from schedules.views import AppointmentCreateListAPIView, AppoitmentRetrieveUpdateDestroyAPIView, UserAppointmentsAPIView, AvailibleSlotsAPIView


urlpatterns = [
    path('api/appointment/', AppointmentCreateListAPIView.as_view(), name='appointment-create-list'),
    path('api/appointment/<int:pk>/', AppoitmentRetrieveUpdateDestroyAPIView.as_view(), name='appointment-detail-view'),
    path('api/users/<str:username>/bookings/', UserAppointmentsAPIView.as_view(), name='user-bookings'),
    path('api/availible-slots/', AvailibleSlotsAPIView.as_view(), name='availible-slots'),

    # Urls para o site.

]
