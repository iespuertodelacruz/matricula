# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170507_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edulevel',
            name='enrollment_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
