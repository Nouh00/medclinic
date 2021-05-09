from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .decorators import unauthenticated_user
from appointments.models import appointment
from patients.models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

@unauthenticated_user
def signup_view(request):
    error = " "
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            doctor_group = Group.objects.get(name='doctor')
            secretary_group = Group.objects.get(name='secretary')
            if request.POST.get('type') == 'doctor':
                user.groups.add(doctor_group)
                login(request, user)
                return redirect('appointments:appointments')
            else:
                if request.POST.get('type') == 'secretary':
                    user.groups.add(secretary_group)
                    login(request, user)
                    return redirect('appointments:appointments') 
                
    else:
        error = "Please select account type"
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form, 'error_msg':error})

@unauthenticated_user
def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:    
                return redirect('appointments:appointments')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('accounts:index')

@login_required
def dashboard(request):
    total_appointments = appointment.objects.filter(patient__isnull=False).count()
    pending_appointments = appointment.objects.filter(appointment_state='Pending', patient__isnull=False).count()
    Approved_appointments = appointment.objects.filter(appointment_state='Approved', patient__isnull=False).count()

    appointments = {
        "pending_appointments":pending_appointments,
        "approved_appointments":Approved_appointments,
        "total_appointments":total_appointments
    }
    return render(request, 'accounts/status.html', appointments)
