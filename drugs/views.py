from django.shortcuts import render,redirect
from .models import drug
from .forms import add_drug_form
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users
# Create your views here.

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def index(request):
    drugs_list = drug.objects.all().order_by('brand')
    drug_form = add_drug_form()
    context = {
        'drug_form':drug_form,
        'drugs_list':drugs_list}
    return render(request, "drugs/index.html", context)


@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def add_drug(request):
    drug_form = add_drug_form()
    if request.method=='POST':
        drug_form = add_drug_form(request.POST)
        if drug_form.is_valid():
            drug_form.save()
            return redirect('drugs:drugs')  
    return render(request, 'drugs:add_drug')

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def edit_drug(request, id):

    _drug = drug.objects.get(id = id)

    drug_form = add_drug_form(instance=_drug)

    if request.method=='POST':
        drug_form = add_drug_form(request.POST,instance=_drug)
        if drug_form.is_valid():
            drug_form.save()
            return redirect('drugs:drugs')
            
    context = {"drug_form":drug_form}          
    return render(request, 'drugs/edit_drug.html', context)

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def delete_drug(request, id):
    drug.objects.get(id=id).delete()
    return redirect('drugs:drugs')