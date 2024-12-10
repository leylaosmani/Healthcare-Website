from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from .forms import AppointmentForm, AvailabilityForm
from .models import Availability
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
           form_data = form.cleaned_data
           print("Form data:", form_data)
           return render(request, 'accounts/success.html', {'form_data': form_data})
    else:
        form = AppointmentForm()
    
    return render(request, 'accounts/book_appointment.html', {'form': form})

@login_required
def set_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.doctor = request.user  
            availability.save()
            
          
            form_data = {
                'day': form.cleaned_data.get('day'),
                'start_time': form.cleaned_data.get('start_time'),
                'end_time': form.cleaned_data.get('end_time'),
            }
            return render(request, 'accounts/availability_success.html', {'form_data': form_data})
    else:
        form = AvailabilityForm()
    
    return render(request, 'accounts/availability.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')