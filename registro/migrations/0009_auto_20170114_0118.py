# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-14 05:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0008_auto_20170114_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Mapa'),
        ),
    ]
