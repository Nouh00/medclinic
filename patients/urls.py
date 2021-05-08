from django.urls import path
from .import views


app_name = 'patients'

urlpatterns = [
    path('', views.index, name='patients'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_patient/book_success/', views.book_success, name='book_success'),
    path('delete_patient/<int:patient_id>/', views.delete_patient, name='delete_patient')
]
