# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0011_auto_20180119_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='observations',
            field=models.TextField(blank=True, null=True, verbose_name='observa\xe7\xf5es'),
        ),
        migrations.AlterField(
            model_name='coursegrid',
            name='date_ini',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='data in\xedcio'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone2',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='telefone 2'),
        ),
    ]
