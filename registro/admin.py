from django.contrib import admin
from registro.models import Registro,Enfermedad,Medico,Consulta
from .forms import RegistradoForm, ConsultaForm
class Registrados(admin.ModelAdmin):
	list_display=('cedula','nombre','apellido','edad','urb','timestamp', 'actualizado',)
	form = RegistradoForm

class Enfermedades (admin.ModelAdmin):
	list_display=('cod_enfermedad','nombre_enfermedad',)

class Medicos (admin.ModelAdmin):
	list_display=('cedula_medico','nombre_medico','apellido_medico',)

class Consultas (admin.ModelAdmin):
	list_display=('fechaConsulta','paciente','medico_tratante','enfermedad_presente',)
	form = ConsultaForm


admin.site.register(Registro,Registrados)
admin.site.register(Enfermedad,Enfermedades)
admin.site.register(Medico,Medicos)
admin.site.register(Consulta,Consultas)