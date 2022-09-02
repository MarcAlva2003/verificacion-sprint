from django.shortcuts import render
from  ITBANK.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Clientes(request):
    projects = Project.objects.all()
    return render(request,'Clientes/Clientes.html')