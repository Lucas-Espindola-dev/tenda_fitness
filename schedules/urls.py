from django.urls import path
from schedules import views


urlpatterns = [
    path('api/appointment/', views.AppointmentCreateListAPIView.as_view(), name='appointment-create-list'),
    path('api/appointment/<int:pk>/', views.AppoitmentRetrieveUpdateDestroyAPIView.as_view(), name='appointment-detail-view'),
    path('api/users/<str:username>/bookings/', views.UserAppointmentsAPIView.as_view(), name='user-bookings'),

    # Urls para o site.
    path('', views.home, name='home'),
    path('appointments/', views.AppointmentListView.as_view(), name='appointments-list'),
    path('appointments/new/', views.AppointmentCreateView.as_view(), name='appointments-create'),
    path('users/<str:username>/appointments/', views.UserAppointmentsListView.as_view(), name='user-appointments-list'),
]
