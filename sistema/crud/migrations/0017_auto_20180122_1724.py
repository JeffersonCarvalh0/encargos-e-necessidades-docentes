# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-22 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0016_activity_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='activity',
            field=models.ManyToManyField(blank=True, null=True, to='crud.Activity', verbose_name='atividade'),
        ),
    ]
