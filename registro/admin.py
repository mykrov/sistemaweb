from django.contrib import admin
from registro.models import Registro
from registro.models import Continent, Country, Location
from .forms import RegistradoForm
class Registrados(admin.ModelAdmin):
	list_display=('cedula','nombre','apellido','edad','urb')
	form = RegistradoForm


admin.site.register(Registro,Registrados)
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Location)