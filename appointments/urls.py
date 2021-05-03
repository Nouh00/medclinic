from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='appointments'),
    path('add-appointment', views.add_appointments, name='add-appointments')

]
