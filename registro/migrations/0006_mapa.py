# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-11 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_auto_20170110_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('path', models.TextField(max_length=2000, null=True)),
            ],
        ),
    ]
