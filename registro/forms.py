from django import forms
from django.forms import ModelForm, Textarea, extras,TextInput,	IntegerField
from .models import Registro, Consulta, Std, Enfermedad,Mapa
from datetime import datetime, timedelta, date
from registro import models
from django.db import models
from django.utils import timezone 	


class RegistradoForm (forms.ModelForm):
	class Meta:
		
		model = Registro
		fields = ["nombre","apellido","cedula","telefono","edad","sexo","municipio","parroquia","urb","direccion",]
		labels={
			'cedula':('Cédula'),'direccion':('Dirección'),'telefono':('Teléfono'),'urb':('Urbanización/Barrio')
		}
		widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Nombres del paciente'}),
            'apellido': TextInput(attrs={'placeholder': 'Apellidos del paciente'}),
            'cedula': TextInput(attrs={'placeholder': 'Sólo números'}),
            'telefono': TextInput(attrs={'placeholder': 'Sólo números'}),
        }
class ConsultaForm (forms.ModelForm):
	class Meta:
		model = Consulta
		fields = ["paciente","enfermedad_presente","tratamiento","observacion","ubicacion","medico_tratante","fecha_consulta",]
		labels = {'observacion':('Observación'),'ubicacion':('Urb/Barrio'),'medico_tratante':'Médico','fecha_consulta':'Fecha de Consulta','enfermedad_presente':'Enfermedad/Caso'}
		widgets = {
            'tratamiento': Textarea(attrs={'cols': 40, 'rows': 10}), 
            'observacion': Textarea(attrs={'cols': 5, 'rows': 2}),
        }

class StdForm (forms.ModelForm):
	class Meta:
		model = Std
		fields = ['nombre_enfermedad','plan',]
		labels={'nombre_enfermedad':'Nombre de Enfer.'}
		widgets = {
            'plan': Textarea(attrs={'cols': 40, 'rows': 10}), 
            
        }

class EnfermedadForm (forms.ModelForm):
	class Meta:
		model = Enfermedad
		fields = ["cod_enfermedad","nombre_enfermedad",]
		labels={'cod_enfermedad':'Cód. de Enfermedad','nombre_enfermedad':'Nombre de Enfer.'}

class MapaForm (forms.ModelForm):
	class Meta:
		model=Mapa
		fields=['name','path',]

class DateForm (forms.Form):
	desde = forms.DateField()
	class Meta:
		labels= {'desde':'Escriba una fecha con el formato Año-Mes-Dia 2016-01-31'}
		widgets = {'desde': forms.DateInput(format=('%Y-%m-%d'),attrs={'placeholder':'d-m-aaaa'}),}

class Formul (forms.ModelForm):
	class Meta:
		model=Consulta
		fields=['fecha_consulta']
		labels= {'fecha_consulta':('Escriba una fecha con el formato Año-Mes-Dia 2016-01-31:'),}
		widgets = {
	    	'desde': forms.DateInput(format=('%Y-%m-%d'),attrs={'placeholder':'d-m-aaaa'}),
	    }
