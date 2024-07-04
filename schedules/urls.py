from django.urls import path
from schedules import views


urlpatterns = [
    path('api/appointment/', views.AppointmentCreateListAPIView.as_view(), name='appointment-create-list'),
    path('api/appointment/<int:pk>/', views.AppoitmentRetrieveUpdateDestroyAPIView.as_view(), name='appointment-detail-view'),
    path('api/users/<str:username>/bookings/', views.UserAppointmentsAPIView.as_view(), name='user-bookings'),
    path('api/availible-slots/', views.AvailibleSlotsAPIView.as_view(), name='availible-slots'),

    # Urls para o site.
    path('appointments/', views.AppointmentListView.as_view(), name='appointments-list'),
]
