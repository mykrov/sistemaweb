from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .forms import RegistradoForm, ConsultaForm
from .models import Registro, Enfermedad, Consulta
from chartit import DataPool, Chart


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
	context = {
		"formulario":formulario
	}
	return render(request,'manuel.html',context)

def consulta (request):
		
	#formulario usado forms.ModelForm
	formularioConsulta = ConsultaForm(request.POST or None)
	
	if formularioConsulta.is_valid():
		formularioConsulta.save()
	contexto = {
		"formularioConsulta":formularioConsulta
	}
	return render(request,'consulta.html',contexto)

def buscar_paciente (request, ci):
	paciente = Registro.objects.get(cedula=ci)
	if request.method == 'GET':
		form = RegistradoForm(instance=paciente)
		table = Consulta.objects.filter(paciente=ci)
		#esta es para generar el nombre del paciente para el html
		nombre_paciente = paciente.nombre + ' '+paciente.apellido
		#muestro el nombre del paciente consultado por consola
		print ('consulta a: '+ paciente.nombre + ' '+paciente.apellido)

	else:
		form = RegistradoForm(request.POST, instance=paciente)
		if form.is_valid():
			form.save()
		#return redirect	('registro:manuel')
		#paso todos los contextos, primero el formulario, luego pra crear la tabla y ultimo el nombre para el html
	contexto = {"form":form, "table":table, "nombre_paciente":nombre_paciente,}
	return render(request,'buscar.html',contexto)	

def estadistica1 (request):
	#se buscan los datos necesarios para el grafico
	datos=DataPool(
		series=
		[{'options':{
			'source': Consulta.objects.all()},
			'terms':['enfermedad_presente','fecha_consulta']}
		])
	#se especifica el grafico
	grafica=Chart(
		datasource = datos,
		series_options =
			[{'options':{'type':'line','stacking':False},
			'terms':{
				'fecha_consulta':['enfermedad_presente']
			}}],
		chart_options =
			{'tittle':{'text':'Estadisticas para'},
			'xAxis': {
				'tittle':{
				'text': 'enfermedad'}}})
	#Mandamos el Grafico
	context = {'grafico':grafica}
	return render (request, 'grafico.html',context )