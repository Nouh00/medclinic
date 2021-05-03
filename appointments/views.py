from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'appointments/index.html')


def add_appointments(request):
    return render(request, 'expanses/add-appointments.html')