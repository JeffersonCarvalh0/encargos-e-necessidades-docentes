#encoding: utf-8

from __future__ import unicode_literals
from django.db import models

#
# Campus
#
class Campus(models.Model):
    name = models.CharField('nome', max_length=50)
    short_name = models.CharField('nome curto', max_length=30)
    add_street = models.CharField('rua', max_length=50)
    add_no = models.IntegerField('número')
    add_neighbor = models.CharField('bairro', max_length=50)
    add_city = models.CharField('cidade', max_length=50)
    add_uf = models.CharField('estado', max_length=2)
    add_zip = models.CharField('CEP', max_length=50)
    phone1 = models.CharField('telefone 1', max_length=14)
    phone2 = models.CharField('telefone 2', max_length=14)
    email = models.EmailField('e-mail')
    site = models.URLField()
    active = models.BooleanField('ativo')

    def __unicode__(self):
        return self.short_nome

    class Meta:
        verbose_name_plural = "Campus"

#
# Curso
#
class Course(models.Model):
    name = models.CharField('nome', max_length=50)
    short_name = models.CharField('nome curto', max_length=20)
    campus = models.ForeignKey(Campus)
    active = models.BooleanField('ativo')

    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = "cursos"

#
# Matriz
#
class CourseGrid(models.Model):
    name = models.CharField('nome', max_length=50)
    course = models.ForeignKey('curso', Course)
    date_ini = models.DateField('data início', null=True)
    date_term = models.DateField('data término', null=True)
    active = models.BooleanField('ativo')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Grade curricular'
        verbose_name_plural = "Grades curriculares"

#
# Area
#
class Area(models.Model):
    name = models.CharField('nome', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = "Áreas"

#
# Disciplina
#
class Discipline(models.Model):
    name = models.CharField('nome', max_length=50)
    short_name = models.CharField('nome curto', max_length=20)
    grid = models.ForeignKey('grade curricular', CourseGrid)
    area = models.ForeignKey('área', Area)
    ementa = models.TextField()
    block = models.SmallIntegerField('bloco')
    work_load = models.SmallIntegerField('carga horária')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = "Disciplinas"


#
# Titulação
#
class Title(models.Model):
    name = models.CharField('nome', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Titulação'
        verbose_name_plural = "Titulações"

#
# TipoContrato
#
class ContractType(models.Model):
    name = models.CharField('nome', max_length=50)
    wk_teaching = models.IntegerField('carga horária de ensino')
    wk_resext = models.IntegerField('carga horária de extensão')
    wk_compl = models.IntegerField('carga horária complementar')
    active = models.BooleanField('ativo')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de contrato'
        verbose_name_plural = "Tipos de contrato"

#
# NaturezaAtividade
#
class ActivityNature(models.Model):
    name = models.CharField('nome', max_length=50)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name: 'Natureza da atividade'
        verbose_name_plural = "Naturezas de atividades"

#
# TipoAtividade
#
class ActivityType(models.Model):
    name = models.CharField('nome', max_length=50)
    wk_week = models.IntegerField('carga horária semanal')
    wk_limit = models.IntegerField('carga horária limite')
    nature = models.ForeignKey('natureza', ActivityNature)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de atividade'
        verbose_name_plural = "Tipos de atividades"


#
# Professor
#
class Teacher(models.Model):
    name = models.CharField('nome', max_length=80)
    course = models.ForeignKey('curso', Course)
    title = models.ForeignKey('títulação', Title)
    area = models.ManyToManyField('área', Area)
    contract_type = models.ForeignKey('tipo de contrato', ContractType)
    phone1 = models.CharField('telefone 1', max_length=14)
    phone2 = models.CharField('telefone 2', max_length=14)
    email = models.EmailField('e-mail')
    active = models.BooleanField('ativo')
    efetivo = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Professor(a)'
        verbose_name_plural = "Professores"


#
# Atividade
#
class Activity(models.Model):
    teacher = models.ForeignKey('professor(a)', Teacher)
    act_type = models.ForeignKey('tipo de atividade', ActivityType)
    quantity = models.IntegerField('quantidade')
    date_ini = models.DateField('data inicial')
    date_term = models.DateField('data final')
    observations = models.TextField('observações')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = "Atividades"

"""
class User(models.Model):
    name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Users"
"""

#
# Periodo
#
class Semester(models.Model):
    name = models.CharField(max_length=50)
    date_ini = models.DateField()
    date_term = models.DateField()

#
# Oferta
#
class Offer(models.Model):
    name = models.CharField(max_length=50)
    semester = models.ForeignKey(Semester)
    course = models.ForeignKey(Course)
    date_ini = models.DateField()
    date_term = models.DateField()

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Offers"

#
# Encargo
#
class Enrollment(models.Model):
    offer = models.ForeignKey(Offer)
    discipline = models.ForeignKey(Discipline)
    teacher = models.ForeignKey(Teacher)

    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Enrolments"
