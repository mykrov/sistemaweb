# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 09:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0013_auto_20160615_0430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='fecha',
            new_name='fechaConsulta',
        ),
    ]
