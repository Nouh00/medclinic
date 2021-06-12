from django.urls import path
from .import views

app_name ='consultations'

urlpatterns = [
    path('', views.index, name='consultations'),
    path('view_consult/<int:consult_id>', views.view_consult, name='view_consult'),
    path('add_consult', views.add_consult, name='add_consult'),
]

