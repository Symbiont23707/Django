from django.shortcuts import render

# Create your views here.
def default_views(request):
    return render(request,'first_app/example.html')

def variable_views(request):
    return render(request,'first_app/variable.html')