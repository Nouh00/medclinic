from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='patients'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('delete_patient/<int:patient_id>/', views.delete_patient, name='delete_patient')
]
