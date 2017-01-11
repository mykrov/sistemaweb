from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count,Avg
from django.http import HttpResponse,Http404, HttpResponseRedirect
from .forms import RegistradoForm, ConsultaForm, EnfermedadForm, StdForm
from .models import Registro, Enfermedad, Consulta, Std
from django.views.generic import TemplateView
from django.core import serializers
from django.contrib import messages
from datetime import datetime, timedelta
from django.forms.models import inlineformset_factory
from .serializers import ConsultaSerializer, UserSerializer, RegistroSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User

# Create your views here.

#Vista del Login
def inicio (request):
	return render(request,'login.html',{})


#Registrar un nuevo Paciente
def manuel (request):
	formulario = RegistradoForm(request.POST or None)
	if formulario.is_valid():
		formulario.save()
		messages.success(request, 'El Paciente Fué Guardado con Éxito')
		return HttpResponseRedirect('/manuel/') 
	context = {"formulario":formulario}
	return render(request,'manuel.html',context)

# Generar una consulta Medica
def consulta (request):
		
	#formulario usado forms.ModelForm
	formularioConsulta = ConsultaForm(request.POST or None)
	
	if formularioConsulta.is_valid():
		formularioConsulta.save()
		messages.success(request, 'Consulta Guardada con Éxito') 
		return HttpResponseRedirect('/consulta/')
	contexto = {"formularioConsulta":formularioConsulta}
	return render(request,'consulta.html',contexto)


#Buscar unpaciente por numero de Cedula
def buscar_paciente (request):
	search = request.POST['busqueda']
	try:
		paciente = Registro.objects.get(cedula=search)
		if request.method == 'POST':
			form = RegistradoForm(instance=paciente)
			table = Consulta.objects.filter(paciente=search)
			#esta es para generar el nombre del paciente para el html
			nombre_paciente = paciente.nombre + ' '+paciente.apellido
			#muestro el nombre del paciente consultado por consola
			print ('consulta a: '+ paciente.nombre + ' '+paciente.apellido)
			print (search)		
	except Registro.DoesNotExist:
		messages.warning(request, 'El Paciente no Existe,desea Registarlo?')
		return HttpResponseRedirect('/manuel/')

	#paso todos los contextos, primero el formulario, luego pra crear la tabla y ultimo el nombre para el html
	contexto = {"form":form, "table":table, "nombre_paciente":nombre_paciente,}
	return render(request,'buscar.html',contexto)

def estadistica1 (request):
	#consulta total
	datos = Consulta.objects.values("enfermedad_presente__nombre_enfermedad").annotate(Count("enfermedad_presente"))
	#Consulta por rango de fechas
	desde='2016-01-01'
	hasta='2016-10-21'
	rango= '%s %s %s' 	%(desde,'a',hasta)
	d= Consulta.objects.filter(fecha_consulta__range=[desde,hasta]).values('enfermedad_presente__nombre_enfermedad')
	x= d.annotate(Count('enfermedad_presente__nombre_enfermedad'))
	context = {'datos': datos,'porfecha':x,'desde':desde,'hasta':hasta, 'rango':rango }
	return render (request, 'grafico.html',context)

def estadistica2 (request):
	#Datos de la semana
	semana = datetime.today() - timedelta(days=7)
	hoy = datetime.today()
	week = Consulta.objects.filter(fecha_consulta__gte=semana).values('enfermedad_presente__nombre_enfermedad')
	x=week.annotate(Count('enfermedad_presente__nombre_enfermedad'))
	contexto = {'porfecha':x,'semana':semana}
	return render (request, 'graficos2.html',contexto)

#vista del mapa
def mapa (request):
	semana = datetime.today() - timedelta(days=7)
	hoy = datetime.today()
	week = Consulta.objects.filter(fecha_consulta__gte=semana).values('paciente__urb')
	x=week.annotate(Count('paciente__urb'))
	print (x)
	contexto={'datos':x,'desde': semana,}
	return render (request,'mapa.html', contexto)

#Crear un plan para las enfermedades
def std (request):
	formulario = StdForm(request.POST or None)
	formulario2 = EnfermedadForm(request.POST or None)
	if formulario.is_valid():
		formulario.save()
		messages.success(request, 'Plan Guardado con Exito')
		return HttpResponseRedirect('/std/') 
	context = {"formulario":formulario}
	return render(request,'std.html',context)


#Agregrar enfermedades a la Base de Datos
def addenf (request):
	formulario2 = EnfermedadForm(request.POST or None)
	if formulario2.is_valid():
		formulario2.save()
		messages.success(request, 'Enfermedad Guardada con Exito')
		return HttpResponseRedirect('/addenf/') 
	context = {"formulario2":formulario2}
	return render(request,'addenf.html',context)

def modificarplan():
	contexto={}
	return render(request,'modplan.html',contexto)

def jsonmap (request):
	semana = datetime.today() - timedelta(days=7)
	hoy = datetime.today()
	week = Consulta.objects.filter(fecha_consulta__gte=semana)
	t=week.annotate(Count('paciente__urb'))
	print(t)
	data = serializers.serialize ('json',t)	
	return HttpResponse (data,content_type='application/json')

class ConsultaViewSet (viewsets.ModelViewSet):
	queryset = Consulta.objects.all()
	serializer_class = ConsultaSerializer

class UserViewSet (viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class RegistroViewSet (viewsets.ModelViewSet):
	queryset = Registro.objects.all()
	serializer_class = RegistroSerializer