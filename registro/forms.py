from django import forms
from django.forms import ModelForm, Textarea, extras
from .models import Registro, Consulta
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
		fields = ["paciente","enfermedad_presente","tratamiento","observacion","medico_tratante",]
		widgets = {
            'tratamiento': Textarea(attrs={'cols': 40, 'rows': 10}), 
            'observacion': Textarea(attrs={'cols': 5, 'rows': 2}),
        }