from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def registrop (request):
	return HttpResponse('Hola esto es el registro de un paciente')
