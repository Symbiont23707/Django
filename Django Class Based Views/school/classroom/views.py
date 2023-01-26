from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"
