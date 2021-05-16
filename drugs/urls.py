from django.urls import path
from .import views

app_name ='drugs'

urlpatterns = [
    path('', views.index, name='drugs'),
]

