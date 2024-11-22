from django import forms
from .models import Availability

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email Address")
    phone = forms.CharField(max_length=15, label="Phone Number")
    appointment_date = forms.DateField(widget=forms.SelectDateWidget(), label="Appointment Date")
    appointment_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label="Appointment Time")
    notes = forms.CharField(widget=forms.Textarea, required=False, label="Additional Notes")

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['day', 'start_time', 'end_time']
        widgets = {
            'day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }