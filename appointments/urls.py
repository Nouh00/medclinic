from django.urls import path
from .import views

app_name ='appointments'

urlpatterns = [
    path('', views.index, name='appointments'),
    path('add-appointment/', views.add_appointments, name='add-appointment'),
    path('add-appointment/book_success/', views.book_success, name='book_success'),

]
