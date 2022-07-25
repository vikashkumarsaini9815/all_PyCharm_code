from django.urls import path
from vsapp import  views

urlpatterns = [
    path('',views.Ram, name = "ram")
]