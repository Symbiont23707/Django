from django.shortcuts import render
from . import models

# Create your views here.

def list_patients(request):
    list_patients = models.Patient.objects.all()
    context = {'patients':list_patients}
    return render(request,'first_app/patients.html',context=context)
