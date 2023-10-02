from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor,Appointment
from .serializers import DoctorSerializer,AppointmentSerializer
# Create your views here.


class DoctorView(viewsets.ModelViewSet):
    serializer_class=DoctorSerializer
    queryset=Doctor.objects.all()


class AppointmentView(viewsets.ModelViewSet):
    serializer_class=AppointmentSerializer
    queryset=Appointment.objects.all()    