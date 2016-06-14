from django.db import models
from smart_selects.db_fields import ChainedForeignKey

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
class Registro(models.Model):
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	cedula=models.IntegerField(default=1)
	telefono=models.CharField(max_length=11,blank=True,null=True)
	edad=models.IntegerField(default=1)
	sexo=models.CharField(max_length=6, choices=SEX_CHOICES)
	municipio=models.CharField(max_length=50, choices=MUNICIPIO_CHOICES)
	parroquia=models.CharField(max_length=50, choices=PARROQUIA_CHOICES)
	urb=models.CharField(max_length=50, choices=URB_CHOICES)
	direccion=models.CharField(max_length=50)
	timestamp = models.DateTimeField (auto_now_add=True, auto_now=False,null=True)
	actualizado = models.DateTimeField (auto_now_add=False, auto_now=True,null=True)

	def __str__(self):
		return '%s %s' %(self.nombre,self.apellido)

class Continent(models.Model):
        name = models.CharField(max_length=255)
        def __str__(self):
        	return self.name

class Country(models.Model):
        continent = models.ForeignKey(Continent)
        name = models.CharField(max_length=255)
        def __str__(self):
        	return self.name

class Location(models.Model):
    continent = models.ForeignKey(Continent)
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
    	return self.name
    
    
  