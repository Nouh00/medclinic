from django.shortcuts import render
from .forms import consul_form
from .models import consultation
# Create your views here.
def index(request):
    consult_form = consul_form()
    return render(request, "consultation/index.html")