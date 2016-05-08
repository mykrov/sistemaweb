from django.contrib import admin
from registro.models import Registro
class Registrados(admin.ModelAdmin):
	list_display=('nombre','apellido','cedula')


admin.site.register(Registro,Registrados)
