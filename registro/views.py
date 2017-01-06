from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count,Avg
from django.http import HttpResponse,Http404, HttpResponseRedirect
from .forms import RegistradoForm, ConsultaForm
from .models import Registro, Enfermedad, Consulta
from django.views.generic import TemplateView
from django.core import serializers
from django.contrib import messages
from datetime import datetime, timedelta


# Create your views here.

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
		messages.success(request, 'El Paciente Fué Guardado con Éxito')
		return HttpResponseRedirect('/manuel/') 
	context = {"formulario":formulario}
	return render(request,'manuel.html',context)

def consulta (request):
		
	#formulario usado forms.ModelForm
	formularioConsulta = ConsultaForm(request.POST or None)
	
	if formularioConsulta.is_valid():
		formularioConsulta.save()
		messages.success(request, 'Consulta Guardada con Éxito') 
		return HttpResponseRedirect('/consulta/')
	contexto = {"formularioConsulta":formularioConsulta}
	return render(request,'consulta.html',contexto)

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