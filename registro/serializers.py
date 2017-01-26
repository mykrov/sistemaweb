from rest_framework import serializers
from .models import Consulta, Registro
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username',)	

class RegistroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Registro
		fields = ('nombre','apellido','cedula','edad','sexo','urb',)

class ConsultaSerializer(serializers.ModelSerializer):
	#sexo = serializers.SlugRelatedField(many=True, read_only=True,slug_field='sexo')

	class Meta:
		model = Consulta
		fields = ('fecha_consulta','paciente','sexo',)
