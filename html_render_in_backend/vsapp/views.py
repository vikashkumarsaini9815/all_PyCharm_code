from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.


def Ram (request):
    page = "hi my name is vicky"
   # return HttpResponse(page,) 
    return render(request, 'index.html')



