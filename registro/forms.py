from django import forms
from django.forms import ModelForm, Textarea, extras
from .models import Registro, Consulta, Std, Enfermedad
from datetime import datetime
from registro import models
from django.db import models



class RegistradoForm (forms.ModelForm):
	class Meta:
		
		model = Registro
		fields = ["nombre","apellido","cedula","telefono","edad","sexo","municipio","parroquia","urb","direccion",]
		

class ConsultaForm (forms.ModelForm):
	class Meta:
		
		model = Consulta
		fields = ["paciente","enfermedad_presente","tratamiento","observacion","medico_tratante","fecha_consulta",]
		widgets = {
            'tratamiento': Textarea(attrs={'cols': 40, 'rows': 10}), 
            'observacion': Textarea(attrs={'cols': 5, 'rows': 2}),
        }

class StdForm (forms.ModelForm):
	class Meta:
		model = Std
		fields = ['nombre_enfermedad','plan',]
		widgets = {
            'plan': Textarea(attrs={'cols': 40, 'rows': 10}), 
            
        }

class EnfermedadForm (forms.ModelForm):
	class Meta:
		model = Enfermedad
		fields = ["cod_enfermedad","nombre_enfermedad",]