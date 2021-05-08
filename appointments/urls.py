from django.urls import path
from .import views

app_name ='appointments'

urlpatterns = [
    path('', views.index, name='appointments'),
    path('add-appointment/', views.add_appointments, name='add-appointment'),
    path('add-appointment/book_success/', views.book_success, name='book_success'),
    path('delete_appointment/<int:patient_id>/', views.delete_appointment, name='delete_appointment'),
    path('change_state/<int:patient_id>/', views.change_state, name='change_state')
]
