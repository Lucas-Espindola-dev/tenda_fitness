from django.urls import path
from schedules.views import AppointmentCreateListView, AppoitmentRetrieveUpdateDestroyView


urlpatterns = [
    path('appointment/', AppointmentCreateListView.as_view(), name='appointment-create-list'),
    path('appointment/<int:pk>/', AppoitmentRetrieveUpdateDestroyView.as_view(), name='appointment-detail-view'),
]