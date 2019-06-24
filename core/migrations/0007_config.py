# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-23 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170507_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_enroll_start_date', models.DateField()),
                ('regular_enroll_end_date', models.DateField()),
                ('exist_ampa', models.BooleanField()),
            ],
        ),
    ]