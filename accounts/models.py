from django.db import models
from django.contrib.auth.models import User
from django import forms 

class Profile(models.Model):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('patient', 'Patient'),
    ]
#this links each profile to 1 user
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
#this is where the roles are defined with 3 roles(choices)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Availability(models.Model):
    doctor = models.ForeignKey(User, related_name='availabilities', on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.doctor.username} - {self.day}: {self.start_time} to {self.end_time}'