# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 04:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0015_auto_20160615_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fechaConsulta',
            field=models.DateField(default=datetime.datetime(2016, 6, 18, 0, 55, 49, 468031)),
        ),
        migrations.AlterField(
            model_name='registro',
            name='actualizado',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]