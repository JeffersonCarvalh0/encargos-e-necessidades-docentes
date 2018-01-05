#encoding: utf-8

from __future__ import unicode_literals
from django.db import models

#
# Campus
#
class Campus(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=30)
    add_street = models.CharField(max_length=50)
    add_no = models.IntegerField()
    add_neighbor = models.CharField(max_length=50)
    add_city = models.CharField(max_length=50)
    add_uf = models.CharField(max_length=2)
    add_zip = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=14)
    phone2 = models.CharField(max_length=14)
    email = models.EmailField()
    site = models.URLField()
    active = models.BooleanField()

    def __unicode__(self):
        return self.short_nome

    class Meta:
        verbose_name_plural = "Campus"

#
# Curso
#
class Course(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)
    campus = models.ForeignKey(Campus)
    active = models.BooleanField()

    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Courses"

#
# Matriz
#
class CourseGrid(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course)
    date_ini = models.DateField(null=True)
    date_term = models.DateField(null=True)
    active = models.BooleanField()

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "CourseGrids"

#
# Area
#
class Area(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Areas"

#
# Disciplina
#
class Discipline(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)
    grid = models.ForeignKey(CourseGrid)
    area = models.ForeignKey(Area)
    ementa = models.TextField()
    block = models.SmallIntegerField()
    work_load = models.SmallIntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Disciplines"


#
# Titulação
#
class Title(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Titles"

#
# TipoContrato
#
class ContractType(models.Model):
    name = models.CharField(max_length=50)
    wk_teaching = models.IntegerField()
    wk_resext = models.IntegerField()
    wk_compl = models.IntegerField()
    active = models.BooleanField()

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Contract Types"

#
# NaturezaAtividade
#
class ActivityNature(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Activity Natures"

#
# TipoAtividade
#
class ActivityType(models.Model):
    name = models.CharField(max_length=50)
    wk_week = models.IntegerField()
    wk_limit = models.IntegerField()
    nature = models.ForeignKey(ActivityNature)

    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Activity Types"


#
# Professor
#
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    course = models.ForeignKey(Course)
    title = models.ForeignKey(Title)
    area = models.ManyToManyField(Area)
    contract_type = models.ForeignKey(ContractType)
    phone1 = models.CharField(max_length=14)
    phone2 = models.CharField(max_length=14)
    email = models.EmailField()
    active = models.BooleanField()
    efetivo = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Teachers"


#
# Atividade
#
class Activity(models.Model):
    teacher = models.ForeignKey(Teacher)
    act_type = models.ForeignKey(ActivityType)
    quantity = models.IntegerField()
    date_ini = models.DateField()
    date_term = models.DateField()
    observations = models.TextField()

    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Activities"

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
