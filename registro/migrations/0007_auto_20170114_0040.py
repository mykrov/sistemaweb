# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-14 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_mapa'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='ubicacion',
            field=models.CharField(choices=[('12 de Marzo', '12 de Marzo'), ('12 de Marzo II', '12 de Marzo II'), ('12 de Octubre', '12 de Octubre'), ('2 de Diciembre', '2 de Diciembre'), ('Beltran Lucena', 'Beltran Lucena'), ('Buena Ventura', 'Buena Ventura'), ('Buena Vista', 'Buena Vista'), ('Chico Toro', 'Chico Toro'), ('La Ceiba', 'La Ceiba'), ('Conticinio', 'Conticinio'), ('El Centro', 'El Centro'), ('El Centro 2', 'El Centro 2'), ('El Mercadito', 'El Mercadito'), ('El Nazareno', 'El Nazareno'), ('El Retruque', 'El Retruque'), ('Las Esmeraldas', 'Las Esmeraldas'), ('La Manga', 'La Manga'), ('Las Trinitarias', 'Las Trinitarias'), ('Libertador', 'Libertador'), ('Barrio Nuevo', 'Barrio Nuevo'), ('Pueblo Viejo', 'Pueblo Viejo'), ('Romulo Betancourt', 'Romulo Betancourt'), ('Valle Verde', 'Valle Verde'), ('Cacerio Los Mangos', 'Cacerio Los Mangos'), ('Cacerio Campo Alegre', 'Cacerio Campo Alegre'), ('Cacerio Cruz Blanca', 'Cacerio Cruz Blanca'), ('Cacerio Las Guayabitas', 'Cacerio Las Guayabitas'), ('Cacerio Los Mereyes', 'Cacerio Los Mereyes'), ('Cacerio Masparro', 'Cacerio Masparro'), ('Sector Aguas  Blancas', 'Sector Aguas  Blancas'), ('Sector Algarrobo', 'Sector Algarrobo'), ('Sector Eucalipto', 'Sector Eucalipto'), ('Sector Mata de Mango', 'Sector Mata de Mango'), ('Sector Melenero', 'Sector Melenero'), ('San Rafael', 'San Rafael'), ('Sector Soco', 'Sector Soco'), ('Sector Tinaja', 'Sector Tinaja'), ('Otro', 'Otro')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='urb',
            field=models.CharField(choices=[('12 de Marzo', '12 de Marzo'), ('12 de Marzo II', '12 de Marzo II'), ('12 de Octubre', '12 de Octubre'), ('2 de Diciembre', '2 de Diciembre'), ('Beltran Lucena', 'Beltran Lucena'), ('Buena Ventura', 'Buena Ventura'), ('Buena Vista', 'Buena Vista'), ('Chico Toro', 'Chico Toro'), ('La Ceiba', 'La Ceiba'), ('Conticinio', 'Conticinio'), ('El Centro', 'El Centro'), ('El Centro 2', 'El Centro 2'), ('El Mercadito', 'El Mercadito'), ('El Nazareno', 'El Nazareno'), ('El Retruque', 'El Retruque'), ('Las Esmeraldas', 'Las Esmeraldas'), ('La Manga', 'La Manga'), ('Las Trinitarias', 'Las Trinitarias'), ('Libertador', 'Libertador'), ('Barrio Nuevo', 'Barrio Nuevo'), ('Pueblo Viejo', 'Pueblo Viejo'), ('Romulo Betancourt', 'Romulo Betancourt'), ('Valle Verde', 'Valle Verde'), ('Cacerio Los Mangos', 'Cacerio Los Mangos'), ('Cacerio Campo Alegre', 'Cacerio Campo Alegre'), ('Cacerio Cruz Blanca', 'Cacerio Cruz Blanca'), ('Cacerio Las Guayabitas', 'Cacerio Las Guayabitas'), ('Cacerio Los Mereyes', 'Cacerio Los Mereyes'), ('Cacerio Masparro', 'Cacerio Masparro'), ('Sector Aguas  Blancas', 'Sector Aguas  Blancas'), ('Sector Algarrobo', 'Sector Algarrobo'), ('Sector Eucalipto', 'Sector Eucalipto'), ('Sector Mata de Mango', 'Sector Mata de Mango'), ('Sector Melenero', 'Sector Melenero'), ('San Rafael', 'San Rafael'), ('Sector Soco', 'Sector Soco'), ('Sector Tinaja', 'Sector Tinaja'), ('Otro', 'Otro')], max_length=50),
        ),
    ]
