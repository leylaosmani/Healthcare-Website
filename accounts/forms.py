from django import forms

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email Address")
    phone = forms.CharField(max_length=15, label="Phone Number")
    appointment_date = forms.DateField(widget=forms.SelectDateWidget(), label="Appointment Date")
    appointment_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label="Appointment Time")
    notes = forms.CharField(widget=forms.Textarea, required=False, label="Additional Notes")
