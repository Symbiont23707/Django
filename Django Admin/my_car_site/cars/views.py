from django.shortcuts import render
from . import models

# Create your views here.

def add(request):
    return render(request,"cars/add.html")

def delete(request):
    return render(request,"cars/delete.html")

def list(request):
    all_cars = models.Cars.objects.all()
    context_cars = {"all_car":all_cars}
    return render(request,"cars/list.html",context=context_cars)
