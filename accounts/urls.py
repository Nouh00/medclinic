from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('', views.index, name='index'),

]
