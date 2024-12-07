from django import forms
from .models import Availability

class AppointmentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'})
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
    )
    phone = forms.CharField(
        max_length=15,
        label="Phone Number",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'})
    )
    appointment_date = forms.DateField(
        label="Appointment Date",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    appointment_time = forms.TimeField(
        label="Appointment Time",
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
    )
    notes = forms.CharField(
        label="Reason for Appointment:",
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Any additional information'})
    )

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['day', 'start_time', 'end_time']
        widgets = {
            'day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }