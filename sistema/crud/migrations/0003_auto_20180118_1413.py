# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20180118_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Atividade', 'verbose_name_plural': 'Atividades'},
        ),
        migrations.AlterModelOptions(
            name='activitynature',
            options={'verbose_name': 'Natureza da atividade', 'verbose_name_plural': 'Naturezas de atividades'},
        ),
        migrations.AlterModelOptions(
            name='activitytype',
            options={'verbose_name': 'Tipo de atividade', 'verbose_name_plural': 'Tipos de atividades'},
        ),
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': 'Area', 'verbose_name_plural': 'Areas'},
        ),
        migrations.AlterModelOptions(
            name='contracttype',
            options={'verbose_name': 'Tipo de contrato', 'verbose_name_plural': 'Tipos de contrato'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
        migrations.AlterModelOptions(
            name='coursegrid',
            options={'verbose_name': 'Matriz curricular', 'verbose_name_plural': 'Matrizes curriculares'},
        ),
        migrations.AlterModelOptions(
            name='discipline',
            options={'verbose_name': 'Disciplina', 'verbose_name_plural': 'Disciplinas'},
        ),
        migrations.AlterModelOptions(
            name='enrollment',
            options={'verbose_name': 'Encargo', 'verbose_name_plural': 'Engargos'},
        ),
        migrations.AlterModelOptions(
            name='offer',
            options={'verbose_name': 'Oferta', 'verbose_name_plural': 'Ofertas'},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'verbose_name': 'Periodo', 'verbose_name_plural': 'Periodos'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Professor(a)', 'verbose_name_plural': 'Professores'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'verbose_name': 'Titulacao', 'verbose_name_plural': 'Titulacoes'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='date_ini',
            field=models.DateField(verbose_name='data inicial'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='date_term',
            field=models.DateField(verbose_name='data final'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='observations',
            field=models.TextField(verbose_name='observacoes'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='quantity',
            field=models.IntegerField(verbose_name='quantidade'),
        ),
        migrations.AlterField(
            model_name='activitynature',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='wk_limit',
            field=models.IntegerField(verbose_name='carga horaria limite'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='wk_week',
            field=models.IntegerField(verbose_name='carga horaria semanal'),
        ),
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='add_no',
            field=models.IntegerField(verbose_name='numero'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='active',
            field=models.BooleanField(verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='wk_compl',
            field=models.IntegerField(verbose_name='carga horaria complementar'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='wk_resext',
            field=models.IntegerField(verbose_name='carga horaria de extens\xe3o'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='wk_teaching',
            field=models.IntegerField(verbose_name='carga horaria de ensino'),
        ),
        migrations.AlterField(
            model_name='course',
            name='active',
            field=models.BooleanField(verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_name',
            field=models.CharField(max_length=20, verbose_name='nome curto'),
        ),
        migrations.AlterField(
            model_name='coursegrid',
            name='active',
            field=models.BooleanField(verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='coursegrid',
            name='date_ini',
            field=models.DateField(null=True, verbose_name='data inicio'),
        ),
        migrations.AlterField(
            model_name='coursegrid',
            name='date_term',
            field=models.DateField(null=True, verbose_name='data termino'),
        ),
        migrations.AlterField(
            model_name='coursegrid',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='block',
            field=models.SmallIntegerField(verbose_name='bloco'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='short_name',
            field=models.CharField(max_length=20, verbose_name='nome curto'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='work_load',
            field=models.SmallIntegerField(verbose_name='carga horaria'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='date_ini',
            field=models.DateField(verbose_name='data inicial'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='date_term',
            field=models.DateField(verbose_name='data final'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='date_ini',
            field=models.DateField(verbose_name='data inicial'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='date_term',
            field=models.DateField(verbose_name='data final'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='active',
            field=models.BooleanField(verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=80, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone1',
            field=models.CharField(max_length=14, verbose_name='telefone 1'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone2',
            field=models.CharField(max_length=14, verbose_name='telefone 2'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
    ]