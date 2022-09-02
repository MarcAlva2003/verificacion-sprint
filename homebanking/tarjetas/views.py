from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tarjetas.models import Tarjetas
from tarjetas.serializer import TarjetaSerializer

# Create your views here.
@login_required
def tarjetas(request):
    projects = Project.objects.all()
    return render(request,'tarjetas/tarjetas.html')
    