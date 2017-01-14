from django.contrib import admin
from registro.models import Registro,Enfermedad,Medico,Consulta,Std,Mapa
from .forms import RegistradoForm, ConsultaForm, StdForm, MapaForm




class Registrados(admin.ModelAdmin):
	list_display=('cedula','nombre','apellido','edad','urb','timestamp', 'actualizado',)
	form = RegistradoForm

class Enfermedades (admin.ModelAdmin):
	list_display=('cod_enfermedad','nombre_enfermedad',)

class Medicos (admin.ModelAdmin):
	list_display=('cedula_medico','nombre_medico','apellido_medico',)

class Consultas (admin.ModelAdmin):
	list_display=('fecha_consulta','paciente','medico_tratante','enfermedad_presente','ubicacion')
	form = ConsultaForm	

class Stdss (admin.ModelAdmin):
	list_display=('nombre_enfermedad','cod_enfermedad','plan',)
	form = StdForm

class Mapas(admin.ModelAdmin):
	list_display=('name',)
	form = MapaForm

admin.site.register(Registro,Registrados)
admin.site.register(Enfermedad,Enfermedades)
admin.site.register(Medico,Medicos)
admin.site.register(Consulta,Consultas)
admin.site.register(Std,Stdss)
admin.site.register(Mapa,Mapas)