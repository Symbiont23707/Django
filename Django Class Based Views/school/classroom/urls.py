from django.urls import path
from .views import HomeView,ThankYouView

app_name = 'classroom'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('thank_you/',ThankYouView.as_view(),name='thank_you')
]
