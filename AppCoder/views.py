from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
# Create your views here.

def curso(request):
    curso2 = Curso(nombre="Diseño", camada=12345)
    curso2.save()
    return HttpResponse(f"Estoy guardando el tercer curso: {curso2.nombre}")