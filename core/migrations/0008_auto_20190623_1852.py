# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-23 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='exist_ampa',
            field=models.BooleanField(verbose_name='¿Existe AMPA?'),
        ),
        migrations.AlterField(
            model_name='config',
            name='regular_enroll_end_date',
            field=models.DateField(verbose_name='Fecha de finalización de matrícula ordinaria'),
        ),
        migrations.AlterField(
            model_name='config',
            name='regular_enroll_start_date',
            field=models.DateField(verbose_name='Fecha de comienzo de matrícula ordinaria'),
        ),
    ]
