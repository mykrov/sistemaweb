# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-09 17:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0022_std'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='std',
            name='nombre_enfermedad',
        ),
    ]