from django.shortcuts import render
from django.http import HttpResponse,Http404
from .forms import RegistradoForm
from .models import Registro

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

#vista de Prueva de forms

def manuel (request):
	formulario = RegistradoForm(request.POST or None)
	if formulario.is_valid():
		formulario.save()
	context = {
		"formulario":formulario
	}
	return render(request,'manuel.html',context)