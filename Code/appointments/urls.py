from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.appointment_create, name='appointment_create'),
    path('', views.appointment_list, name='appointment_list'),
]
