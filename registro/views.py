from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.

#Vista de Prueba para URLs

def registrop (request):
	return HttpResponse('Hola esto es el registro de un paciente')


#Vista del Login

def login (request):
	return HttpResponse('login.html')
