from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Avg, Max,Min,Sum
from django.http import HttpResponse,Http404, HttpResponseRedirect
from .forms import RegistradoForm, ConsultaForm, EnfermedadForm, StdForm, DateForm, Formul
from .models import Registro, Enfermedad, Consulta, Std, Mapa
from django.views.generic import TemplateView
from django.core import serializers
from django.contrib import messages
from datetime import datetime, timedelta, date
from django.utils import timezone
from django.forms.models import inlineformset_factory
from .serializers import ConsultaSerializer, UserSerializer, RegistroSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
import json

# Create your views here.

#Vista del Login
def inicio (request):
	return render(request,'login.html',{})


#Registrar un nuevo Paciente
def manuel (request):
	formulario = RegistradoForm(request.POST or None)
	if formulario.is_valid():
		formulario.save()
		messages.success(request, 'El Paciente fué guardado con éxito')
		return HttpResponseRedirect('/manuel/') 
	context = {"formulario":formulario}
	return render(request,'manuel.html',context)

# Generar una consulta Medica
def consulta (request):
		
	#formulario usado forms.ModelForm
	formularioConsulta = ConsultaForm(request.POST or None)
	
	if formularioConsulta.is_valid():
		formularioConsulta.save()
		messages.success(request, 'Consulta guardada con Éxito') 
		return HttpResponseRedirect('/consulta/')
	contexto = {"formularioConsulta":formularioConsulta}
	return render(request,'consulta.html',contexto)


#Buscar unpaciente por numero de Cedula
def buscar_paciente (request):
	search = request.POST['busqueda']
	try:
		paciente = Registro.objects.get(cedula=search or 1)
		if request.method == 'POST':
			form = RegistradoForm(instance=paciente)
			table = Consulta.objects.filter(paciente=search)
			#esta es para generar el nombre del paciente para el html
			nombre_paciente = paciente.nombre + ' '+paciente.apellido
			#muestro el nombre del paciente consultado por consola
			print ('consulta a: '+ paciente.nombre + ' '+paciente.apellido)
			print (search)		
	except Registro.DoesNotExist:
		messages.warning(request, 'El Paciente no existe,desea Registarlo?')
		return HttpResponseRedirect('/manuel/')

	#paso todos los contextos, primero el formulario, luego pra crear la tabla y ultimo el nombre para el html
	contexto = {"form":form, "table":table, "nombre_paciente":nombre_paciente,}
	return render(request,'buscar.html',contexto)

def estadistica1 (request):
	#consulta total
	datos = Consulta.objects.values("enfermedad_presente__nombre_enfermedad").annotate(Count("enfermedad_presente"))
	
	#Consulta por rango de fechas
	desde='2016-10-01'
	hasta='2017-01-20'
	# comi=datetime.date(2016,1,1,0,0,0)
	# end=datetime.date(2017,1,15,0,0,0)
	rango= '%s %s %s' 	%(desde,'a',hasta)
	d= Consulta.objects.filter(fecha_consulta__range=[desde,hasta]).values('enfermedad_presente__nombre_enfermedad')
	x= d.annotate(Count('enfermedad_presente__nombre_enfermedad'))
	#Consulta de Hombre-Mujer
	hm=Consulta.objects.filter(fecha_consulta__range=[desde,hasta]).extra(select={'date':'fecha_consulta'}).values('paciente_id__sexo').annotate(value=Count('paciente_id__sexo'))
	print(hm)	
	context = {'datos': datos,'porfecha':x,'desde':desde,'hasta':hasta, 'rango':rango,'hm':hm,}
	return render (request, 'grafico.html',context)



def estadistica2 (request):
	#Datos de la semana
	semana = datetime.today() - timedelta(days=7)
	hoy = datetime.today()
	week = Consulta.objects.filter(fecha_consulta__gte=semana).values('enfermedad_presente__nombre_enfermedad')
	x=week.annotate(Count('enfermedad_presente__nombre_enfermedad'))
	w=x.aggregate(Max('enfermedad_presente'))
	contexto = {'porfecha':x,'semana':semana}
	return render (request, 'graficos2.html',contexto)

#vista del mapa
def mapa (request):
	#seteo la fecha
	semana = datetime.today() - timedelta(days=200)
	hoy = datetime.today()	
	#traigo el mapa SVG
	mapa=list(Mapa.objects.all().values('name','path'))
	week = Consulta.objects.filter(fecha_consulta__gte=semana).order_by('enfermedad_presente__nombre_enfermedad')[0]
	x=Consulta.objects.filter(fecha_consulta__gte=semana).values('ubicacion__name','ubicacion__path').annotate(value=Count('ubicacion__name'))
	print(x)
	contexto={'datos':week,'desde': semana,'mapa':mapa,'ser':x}
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

#prueba de creacion de JSON
def jsonmap (request):
	desde='2016-10-01'
	hasta='2017-01-20'
	semana = datetime.today() - timedelta(days=7)
	hoy = datetime.today()
	week = Consulta.objects.filter(fecha_consulta__gte=semana)
	t=week.annotate(value=Count('paciente_id__urb'))
	hm=Consulta.objects.filter(fecha_consulta__range=[desde,hasta]).extra(select={'date':'fecha_consulta'}).values('paciente_id__sexo','date').annotate(value=Count('paciente_id__sexo'))
	k=list(hm)
	print(k)
	data = serializers.serialize ('json',hm,fields=('date','paciente_id__sexo'))	
	return HttpResponse (data,content_type='application/json')

#prueba de API Serializer
class ConsultaViewSet (viewsets.ModelViewSet):
	queryset = Consulta.objects.all()
	serializer_class = ConsultaSerializer

class UserViewSet (viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class RegistroViewSet (viewsets.ModelViewSet):
	queryset = Registro.objects.all()
	serializer_class = RegistroSerializer

#Mostrar los planes de las diferentes enfermedades
def planes (request):
	contexto={}
	desde='2016-01-01'
	hasta='2017-01-20'
	maxima1= Consulta.objects.filter(fecha_consulta__range=[desde,hasta]).values('enfermedad_presente__nombre_enfermedad').annotate(total=Count('enfermedad_presente')).order_by('-total')[0]
	name=maxima1['enfermedad_presente__nombre_enfermedad']
	total=maxima1['total']
	i= Std.objects.filter(nombre_enfermedad__nombre_enfermedad=name).values('plan')
	try:
		plantxt=i[0]['plan']
		contexto={'name':name,'plan':plantxt,'desde':desde,'hasta':hasta,'total':total}
	except:
		messages.warning(request, 'El Plan solicitado No existe')
		plantxt='Por favor solicite a un experto que introduzca un plan para dicho caso.'
		print (plantxt)
		contexto={'name':name,'plan':plantxt,'desde':desde,'hasta':hasta,'total':total}

	
	return render (request,'planes.html',contexto)

def rfecha (request):
	formualriodesde = DateForm()
	try:
		if request.method == 'POST':
			formualriodesde = DateForm(request.POST)
			if formualriodesde.is_valid():
				desde=request.POST.get('desde')
				hasta=date.today()
				rango= '%s %s %s' 	%(desde,'a',hasta)
				d= Consulta.objects.filter(fecha_consulta__range=[desde,hasta]).values('enfermedad_presente__nombre_enfermedad')
				x= d.annotate(Count('enfermedad_presente__nombre_enfermedad'))
				contexto={'formul':formualriodesde, 'porfecha':x,'rango':rango}
			else:
				messages.warning(request, 'El Formato es Año-Mes-Dia Ej: 2016-01-31')
				formualriodesde= DateForm()
				contexto={'formul':formualriodesde,}
		else:
			formualriodesde= DateForm()
			contexto={'formul':formualriodesde,}
	
	except:
		messages.warning(request, 'El Formato es Año-Mes-Dia Ej: 2016-01-31')
		return HttpResponseRedirect('/rfecha/')

	return render (request,'rfecha.html',contexto)