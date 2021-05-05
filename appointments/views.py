from django.shortcuts import render
from .models import appointment
from patients.models import Patient
# Create your views here.

def index(request):
    appointments = appointment.objects.all()
    return render(request, 'appointments/index.html', {"appointments": appointments})


def add_appointments(request):
    return render(request, 'expanses/add-appointments.html')