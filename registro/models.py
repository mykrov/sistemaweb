from django.db import models
from datetime import datetime
from django.utils import timezone

# Opciones de Seleccion para los  formularios de ubicacion.
MUNICIPIO_CHOICES = (
    ('CP', 'Cruz Paredes'),
    ('AAT', 'Alb.ArveloTorrealba'),
    ('BA', 'Barinas'),
    ('OT', 'Otro'),
)

PARROQUIA_CHOICES = (
	('BARR', 'Barrancas'),
	('MASP', 'Masparrito'),
	('SOCO', 'Socorro'),
	('OTRo', 'Otro'),
)

URB_CHOICES = (
	('12m', '12 de Marzo'),
	('12oc', '12 de Octubre'),
	('2dic', '2 de Diciembre'),
	('BelL', 'Beltran Lucena'),
	('BnVen', 'Buena Ventura'),
	('BnVis', 'Buena Vista'),
	('ChiT', 'Chico Toro'),
	('Cont', 'Conticinio'),
	('ElC', 'El Centro'),
	('Merc', 'El Mercadito'),
	('ElNz', 'El Nazareno'),
	('ElRe', 'El Retruque'),
	('LasEs', 'Las Esmeraldas'),
	('LaMan', 'La Manga'),
	('LaTri', 'Las Trinitarias'),
	('LiB', 'Libertador'),
	('BarNue', 'Barrio Nuevo'),
	('PueVi', 'Pueblo Viejo'),
	('RoBet', 'Romulo Betancourt'),
	('ValV', 'Valle Verde'),
	('LosMa', 'Cacerio Los Mangos'),
	('CAALe', 'Cacerio Campo Alegre'),
	('CrzBlan', 'Cacerio Cruz Blanca'),
	('Guay', 'Cacerio Las Guayabitas'),
	('LosMe', 'Cacerio Los Mereyes'),
	('Masp', 'Cacerio Masparro'),
	('AgBl', 'Sector Aguas  Blancas'),
	('Algarr', 'Sector Algarrobo'),
	('Euca', 'Sector Eucalipto'),
	('matMan', 'Sector Mata de Mango'),
	('Melen', 'Sector Melenero'),
	('SanRaf', 'San Rafael'),
	('Soc', 'Sector Soco'),
	('Tinaj', 'Sector Tinaja'),
	('other', 'Otro'),

)
SEX_CHOICES =(
	('M', 'M'),
	('F', 'F'),
)
# Create your models here.
# Modelo usado para los registros de pacientes nuevos. PK se usa la Cedula
class Registro(models.Model):
	nombre=models.CharField(max_length=50)
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

class Consulta(models.Model):
	fecha_consulta = models.DateTimeField(default=timezone.now)
	paciente = models.ForeignKey(Registro, on_delete=models.CASCADE)
	enfermedad_presente=models.ForeignKey(Enfermedad,null=False)
	tratamiento = models.CharField(max_length=100, null=True)
	observacion = models.CharField(max_length=100, null=True)
	medico_tratante = models.ForeignKey(Medico, null=True)
	objects = ManejadorEnfermedad()
	def __str__(self):
		return '%s %s %s' %(self.paciente,self.fecha_consulta,self.enfermedad_presente)






