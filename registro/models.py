from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

# Opciones de Seleccion para los  formularios de ubicacion.
MUNICIPIO_CHOICES = (
    ('CP', 'Cruz Paredes'),
    ('AAT', 'Alb.ArveloTorrealba'),
    ('BA', 'Barinas'),
    ('OT', 'Otro'),
)
deffault='Otra'
PARROQUIA_CHOICES = (
	('BARR', 'Barrancas'),
	('MASP', 'Masparrito'),
	('SOCO', 'Socorro'),
	('OTRo', 'Otro'),
)

URB_CHOICES = (
	('12 de Marzo', '12 de Marzo'),
	('12 de Marzo II', '12 de Marzo II'),
	('12 de Octubre', '12 de Octubre'),
	('2 de Diciembre', '2 de Diciembre'),
	('Beltran Lucena', 'Beltran Lucena'),
	('Buena Ventura', 'Buena Ventura'),
	('Buena Vista', 'Buena Vista'),
	('Chico Toro', 'Chico Toro'),
	('La Ceiba', 'La Ceiba'),
	('Conticinio', 'Conticinio'),
	('El Centro', 'El Centro'),
	('El Centro 2', 'El Centro 2'),
	('El Mercadito', 'El Mercadito'),
	('El Nazareno', 'El Nazareno'),
	('El Retruque', 'El Retruque'),
	('Las Esmeraldas', 'Las Esmeraldas'),
	('La Manga', 'La Manga'),
	('Las Trinitarias', 'Las Trinitarias'),
	('Libertador', 'Libertador'),
	('Barrio Nuevo', 'Barrio Nuevo'),
	('Pueblo Viejo', 'Pueblo Viejo'),
	('Romulo Betancourt', 'Romulo Betancourt'),
	('Valle Verde', 'Valle Verde'),
	('Cacerio Los Mangos', 'Cacerio Los Mangos'),
	('Cacerio Campo Alegre', 'Cacerio Campo Alegre'),
	('Cacerio Cruz Blanca', 'Cacerio Cruz Blanca'),
	('Cacerio Las Guayabitas', 'Cacerio Las Guayabitas'),
	('Cacerio Los Mereyes', 'Cacerio Los Mereyes'),
	('Cacerio Masparro', 'Cacerio Masparro'),
	('Sector Aguas  Blancas', 'Sector Aguas  Blancas'),
	('Sector Algarrobo', 'Sector Algarrobo'),
	('Sector Eucalipto', 'Sector Eucalipto'),
	('Sector Mata de Mango', 'Sector Mata de Mango'),
	('Sector Melenero', 'Sector Melenero'),
	('San Rafael', 'San Rafael'),
	('Sector Soco', 'Sector Soco'),
	('Sector Tinaja', 'Sector Tinaja'),
	('Otro', 'Otro'),

)
SEX_CHOICES =(
	('M', 'M'),
	('F', 'F'),
)
# Create your models here.
# Modelo usado para los registros de pacientes nuevos. PK se usa la Cedula
class Registro(models.Model):
	nombre=models.CharField(max_length=52)
	apellido=models.CharField(max_length=50)
	cedula=models.IntegerField(primary_key=True, unique=True)
	telefono=models.CharField(max_length=11,blank=True,null=True)
	edad=models.IntegerField(default=1)
	sexo=models.CharField(max_length=6, choices=SEX_CHOICES)
	municipio=models.CharField(max_length=50, choices=MUNICIPIO_CHOICES)
	parroquia=models.CharField(max_length=50, choices=PARROQUIA_CHOICES)
	urb=models.CharField(max_length=50, choices=URB_CHOICES)
	direccion=models.CharField(max_length=50)
	timestamp = models.DateTimeField (auto_now_add=True, auto_now=False,null=False)
	actualizado = models.DateTimeField (auto_now_add=False, auto_now=True,null=False)

	def __str__(self):
		return '%s %s %s' %(self.cedula,self.apellido,self.nombre)

class Enfermedad(models.Model):
	cod_enfermedad=models.CharField(max_length=20, primary_key=True, unique=True)
	nombre_enfermedad=models.CharField(max_length=100,null=False)

	def __str__(self):
		return '%s %s' %(self.cod_enfermedad,self.nombre_enfermedad)

class Medico(models.Model):
	nombre_medico=models.CharField(max_length=100, null=True)
	apellido_medico=models.CharField(max_length=100, null=True)
	cedula_medico=models.IntegerField(default=1, primary_key=True, unique=True)
	
	def __str__(self):
		return '%s %s' %(self.cedula_medico,self.nombre_medico)

class ManejadorEnfermedad (models.Manager):
	def contar (self,keyword):
		return self.filter(enfermedad_presente__nombre_enfermedad__icontains=keyword).count()

class Mapa(models.Model):
	name = models.CharField(max_length=100, null=False)
	path = models.TextField(max_length=2000, null=True)
	def __str__(self):
		return '%s' %(self.name)

class Consulta(models.Model):
	fecha_consulta = models.DateTimeField(default=timezone.now)
	paciente = models.ForeignKey(Registro, on_delete=models.CASCADE)
	enfermedad_presente = models.ForeignKey(Enfermedad,null=False)
	tratamiento = models.TextField(max_length=2000, null=True)
	observacion = models.TextField(max_length=2000, null=True)
	medico_tratante = models.ForeignKey(Medico, null=True)
	ubicacion=models.ForeignKey(Mapa, null=False)
	objects = ManejadorEnfermedad()
	def __str__(self):
		return '%s %s %s' %(self.paciente,self.fecha_consulta,self.enfermedad_presente)

class Std(models.Model):
	nombre_enfermedad = models.ForeignKey(Enfermedad,null=True)
	cod_enfermedad = models.CharField(max_length=200, null=True)
	plan = models.TextField(max_length=2000,null=False)
	def __str__(self):
		return '%s %s' %(self.nombre_enfermedad, self.plan)






