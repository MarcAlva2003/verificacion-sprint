from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):    
    return render(request,'ITBANK/home.html')

@login_required
def inversiones(request):
    return render(request,'ITBANK/inversiones.html')

@login_required
def terminos(request):
    return render(request,'ITBANK/terminos.html')

@login_required
def sucycajero(request):
    return render(request,'ITBANK/sucycajero.html')

@login_required
def perfil(request):    
    return render(request,'ITBANK/perfil.html')