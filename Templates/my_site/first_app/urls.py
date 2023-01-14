from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('',views.default_views,name='example'),
    path('variable/',views.variable_views,name='variable')
    ]