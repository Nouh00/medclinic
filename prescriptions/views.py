from patients.views import patient_profile
from django.shortcuts import redirect, render
from .models import prescription
from patients.models import Patient, doctor
from drugs.models import drug
import datetime, json

# Create your views here.
def index(request):
    presc_list = prescription.objects.all()
    patients_list = Patient.objects.all()
    doctors_list = doctor.objects.all()
    drugs_list = drug.objects.all()
    context = {
        "presc_list":presc_list,
        "patients_list":patients_list,
        "doctors_list":doctors_list,
        "drugs_list":drugs_list,
    }
    return render(request, "prescriptions/index.html", context)



def add_prescription(request):
    drugs= []
    if request.method == 'POST':
        for x in range(int(request.POST['drugs_count'])):
            for d,v in request.POST.items():
                if str(d).endswith(str(x)):
                    drugs.append({x:v})
    
        
        doc = doctor.objects.get(doctor_id=request.POST['doctor'])
        patient = Patient.objects.get(patient_id=request.POST['patient'])
        add_presc = prescription.objects.create(
            doctor=doc,
            patient=patient,
            note=request.POST['note'],
            doc_type="prescription",
            drug_data = drugs
            )

        return redirect('prescriptions:prescriptions')
    
def delete_prescription(request, presc_id):
    prescriptions = prescription.objects.get(prescription_id=presc_id).delete()
    return redirect("prescriptions:prescriptions")

def view_presc(request, presc_id):
    prescriptions =prescription.objects.get(prescription_id=presc_id)
    presc_drugs = prescriptions.drug_data
    birth = prescriptions.patient.birth
    td=datetime.datetime.now().date() 
    age = int((td-birth).days /365.25)
    patient_data = {
        'fname': prescriptions.patient.fname,
        'lname': prescriptions.patient.lname,
        'birth': prescriptions.patient.birth,   
        'phone': prescriptions.patient.phone,
        'email': prescriptions.patient.email,   
        'adresse': prescriptions.patient.adresse,
        'age': age
    }
    presc_drugs1= {}
    for x in presc_drugs:
        presc_drugs1 = x

    context={
        "drug_data": json.dumps(presc_drugs),
        "presc_data": prescriptions,
        "patient":patient_data
    }
    return render(request, "prescriptions/prescription-view.html", context)
        

