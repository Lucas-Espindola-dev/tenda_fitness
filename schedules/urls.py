from django.urls import path
from schedules.views import AppointmentCreateListView, AppoitmentRetrieveUpdateDestroyView, UserAppointmentsView, AvailibleSlotsView


urlpatterns = [
    path('api/appointment/', AppointmentCreateListView.as_view(), name='appointment-create-list'),
    path('api/appointment/<int:pk>/', AppoitmentRetrieveUpdateDestroyView.as_view(), name='appointment-detail-view'),
    path('api/users/<str:username>/bookings/', UserAppointmentsView.as_view(), name='user-bookings'),
    path('api/availible-slots/', AvailibleSlotsView.as_view(), name='availible-slots'),

    # Urls para o site.

]
