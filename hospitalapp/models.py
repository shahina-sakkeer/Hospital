from django.db import models

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=200)
    patients_per_day=models.PositiveIntegerField()


    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    patient=models.CharField(max_length=200)

    def __str__(self):
        return self.patient

