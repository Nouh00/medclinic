from django.shortcuts import redirect, render
from .forms import consul_form
from .models import consultation
# Create your views here.
def index(request):
    consult_form = consul_form()
    consultations = consultation.objects.all()
    context = {
        "consult_form":consult_form,
        "consultations":consultations
    }
    return render(request, "consultation/index.html", context)

def add_consultation(request):
    consult_form = consul_form()
    if request.method=='POST':
        consult_form = consul_form(request.POST)
        if consul_form.is_valid():
            consul_form.save()
        return redirect('consultations:consultations')

    return render('consultations:consultations')
