from django.urls import path
from .views import  bus, mtc, home

urlpatterns = [
    path('', mtc, name='mtc'),
    path('ajax/', bus, name='bus'),
    ]