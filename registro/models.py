from django.db import models

# Create your models here.
class Registro(models.Model):
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	cedula=models.IntegerField(default=1)
	telefono=models.CharField(max_length=11,blank=True,null=True)
	edad=models.IntegerField(default=1)
	sexo=models.CharField(max_length=6)
	municipio=models.CharField(max_length=50)
	parroquia=models.CharField(max_length=50)
	urb=models.CharField(max_length=50)
	direccion=models.CharField(max_length=50)

	def __str__(self):
		return '%s %s' %(self.nombre,self.apellido)