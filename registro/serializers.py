from rest_framework import serializers
from .models import Consulta, Registro
from django.contrib.auth.models import User

class ConsultaSerializer(serializers.HyperlinkedModelSerializer):
	 # paciente = serializers.HyperlinkedRelatedField(
	 # 	many = True,
	 # 	read_only = True,
	 # 	view_name='paciente',
	 # 	)
	paciente = serializers.HyperlinkedRelatedField(
	 	queryset=Registro.objects.all(), 
	 	view_name='registro-detail')

	class Meta:
		model = Consulta
		fields = ('fecha_consulta','paciente')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username',)	

class RegistroSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Registro
		fields = ('nombre','apellido','cedula','edad','sexo','urb',)