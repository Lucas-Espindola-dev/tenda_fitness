from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schedules.urls')),
    # path('register/', ..., name='register'),
    path('login/', login_view, name='login'),
    # path('user/<str:username>/'),
    path('logout/', logout_view, name='logout'),
]
