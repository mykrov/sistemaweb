# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 09:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0014_auto_20160615_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fechaConsulta',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 15, 5, 53, 4, 127407)),
        ),
    ]