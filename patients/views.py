from django.shortcuts import render
from .models import Patient

def patient_search(request):
    national_id = request.GET.get('national_id')
    patient = None
    if national_id:
        try:
            patient = Patient.objects.get(national_id=national_id)
        except Patient.DoesNotExist:
            patient = None
    return render(request, 'patients/patient_search.html', {'patient': patient, 'national_id': national_id})
