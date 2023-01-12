from django.urls import path
from . import views
urlpatterns = [
    path('',views.default_views),
    path('variables/',views.variable_views)
    ]