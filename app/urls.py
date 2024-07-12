from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schedules.urls')),
    path('register/', ..., name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user/<str:username>/'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
