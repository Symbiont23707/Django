from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.

def add(request):
    if request.POST:
        brand = request.POST["brand"]
        year = request.POST["year"]
        models.Cars.objects.create(brand=brand,year=year)
        return redirect(reverse("cars:list"))
    else:
        return render(request,"cars/add.html")

def delete(request):
    if request.POST:
        pk = request.POST["pk"]
        try:
            models.Cars.objects.get(pk=pk).delete()
            return redirect(reverse("cars:list"))
        except:
            print(f"PK:{pk} not founded")
            return redirect(reverse("cars:list"))
    else:        
        return render(request,"cars/delete.html")

def list(request):
    all_cars = models.Cars.objects.all()
    context_cars = {"all_cars":all_cars}
    return render(request,"cars/list.html",context=context_cars)
