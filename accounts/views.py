from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .decorators import unauthenticated_user
# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

@unauthenticated_user
def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login
            login(request, user)
            return redirect('appointments:appointments')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

@unauthenticated_user
def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:    
                return redirect('appointments:appointments')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('accounts:index')

