from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.

#Vista de registro de pacientes
def registrop (request):
	return render(request,'registrotabs.html',{})


#Vista del Login
def inicio (request):
	return render(request,'login.html',{})

#vista principal
def historia (request):
	return render(request,'historia.html',{})
