# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0012_auto_20160615_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfermedad',
            name='cod_enfermedad',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
