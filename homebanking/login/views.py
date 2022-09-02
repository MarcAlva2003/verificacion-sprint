from django.shortcuts import render
from .models import Project

# Create your views here.

def login(request):
    projects = Project.objects.all()
    return render(request,'login/login.html')

def register(request):
    
    return render(request,'login/register.html')