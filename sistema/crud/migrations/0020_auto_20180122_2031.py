# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-22 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0019_merge_20180122_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='phone2',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='telefone 2'),
        ),
    ]
