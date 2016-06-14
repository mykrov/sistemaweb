from django import forms
from .models import Registro, Continent, Country, Location

class RegistradoForm (forms.ModelForm):
	class Meta:

		model = Registro
		fields = ["nombre","apellido","cedula","telefono","edad","sexo","municipio","parroquia","urb","direccion",]
	

		

	

