#encoding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now

#
# Campus
#
class Campus(models.Model):
    name = models.CharField('nome', max_length=50)
    short_name = models.CharField('nome curto', max_length=30)
    add_street = models.CharField('rua', max_length=50)
    add_no = models.IntegerField('numero')
    add_neighbor = models.CharField('bairro', max_length=50)
    add_city = models.CharField('cidade', max_length=50)
    add_uf = models.CharField('estado', max_length=2)
    add_zip = models.CharField('CEP', max_length=50)
    phone1 = models.CharField('telefone 1', max_length=14)
    phone2 = models.CharField('telefone 2', max_length=14, null=True)
    email = models.EmailField('e-mail')
    site = models.URLField('site')
    active = models.BooleanField('ativo', default=True)

    def __unicode__(self):
        return self.short_name

    class Meta:
        verbose_name_plural = "Campus"

#
# Curso
#
class Course(models.Model):
    name = models.CharField('nome', max_length=50)
    short_name = models.CharField('nome curto', max_length=20)
    campus = models.ForeignKey(Campus)
    active = models.BooleanField('ativo', default=True)

    def __unicode__(self):
        return self.short_name

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = "cursos"

#
# Matriz
#
class CourseGrid(models.Model):
    name = models.CharField('nome', max_length=50)
    course = models.ForeignKey(Course, verbose_name='curso')
    date_ini = models.DateField('data início', default=now)
    date_term = models.DateField('data término', null=True, blank=True)
    active = models.BooleanField('ativo', default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Matriz curricular'
        verbose_name_plural = "Matrizes curriculares"

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
    grid = models.ForeignKey(CourseGrid, verbose_name='matriz curricular')
    area = models.ForeignKey(Area, verbose_name='área')
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
    active = models.BooleanField('ativo', default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de contrato'
        verbose_name_plural = "Tipos de contrato"

#
# NaturezaAtividade
#
class ActivityNature(models.Model):
    name = models.CharField('nome', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Natureza da atividade'
        verbose_name_plural = "Naturezas de atividades"

#
# TipoAtividade
#
class ActivityType(models.Model):
    name = models.CharField('nome', max_length=50)
    wk_week = models.IntegerField('carga horária semanal')
    wk_limit = models.IntegerField('carga horária limite')
    nature = models.ForeignKey(ActivityNature, verbose_name='natureza')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de atividade'
        verbose_name_plural = "Tipos de atividades"

#
# Atividade
#
class Activity(models.Model):
    # teacher = models.ForeignKey(Teacher, verbose_name='professor(a)')
    act_type = models.ForeignKey(ActivityType, verbose_name='tipo de atividade')
    quantity = models.IntegerField('quantidade')
    date_ini = models.DateField('data inicial')
    date_term = models.DateField('data final')
    observations = models.TextField('observações', null=True)

    def __unicode__(self):
        return self.teacher

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = "Atividades"

#
# Professor
#
class Teacher(models.Model):
    name = models.CharField('nome', max_length=80)
    course = models.ForeignKey(Course, verbose_name='curso')
    title = models.ForeignKey(Title, verbose_name='titulação')
    area = models.ManyToManyField(Area, verbose_name='área')
    contract_type = models.ForeignKey(ContractType, verbose_name='tipo de contrato')
    phone1 = models.CharField('telefone 1', max_length=14)
    phone2 = models.CharField('telefone 2', max_length=14, null=True, blank=True)
    email = models.EmailField('e-mail')
    efetivo = models.BooleanField(default=True)
    activity = models.ManyToManyField(Activity, verbose_name='atividade', blank=True)
    active = models.BooleanField('ativo', default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Professor(a)'
        verbose_name_plural = "Professores"

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
    name = models.CharField('nome', max_length=50)
    date_ini = models.DateField('data inicial')
    date_term = models.DateField('data final')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'

#
# Oferta
#
class Offer(models.Model):
    name = models.CharField('nome', max_length=50)
    semester = models.ForeignKey(Semester, verbose_name='período')
    course = models.ForeignKey(Course, verbose_name='curso')
    date_ini = models.DateField('data inicial')
    date_term = models.DateField('data final')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = "Ofertas"

#
# Encargo
#
class Enrollment(models.Model):
    offer = models.ForeignKey(Offer, verbose_name='oferta')
    discipline = models.ForeignKey(Discipline, verbose_name='disciplina')
    teacher = models.ForeignKey(Teacher, verbose_name='professor(a)')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Encargo'
        verbose_name_plural = "Encargos"
