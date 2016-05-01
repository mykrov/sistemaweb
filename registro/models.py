from django.db import models

# Create your models here.
class registropaciente(models.Models):
	nombre = models.ChartField(max_length=30)
	apellido = models.ChartField(max_length=30)
	cedula = models.IntegerFiel(max_length=30)
	telefono = models.IntegerFiel(max_length=30)
	edad = models.ChartField(max_length=30)
	sexo =  models.ChartField(max_length=10)
	municipio = models.ChartField(max_length=30)
	parroquia = models.ChartField(max_length=15)
	urbarrio = models.ChartField(max_length=15)
	direccion = models.ChartField(max_length=60)