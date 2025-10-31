from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date} {self.appointment_time}"
