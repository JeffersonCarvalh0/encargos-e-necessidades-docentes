# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Campus(models.Model):
    '''
        Campus of the institution
    '''
    name = models.CharField(max_length = 255)
    short_name = models.CharField(max_length = 10)
    telephone1 = models.IntegerField()
    telephone1 = models.IntegerField()
    email = models.EmailField()
    site = models.URLField()
    active = mdoels.BooleanField()
    address = models.ForeignKey('Address', on_delete=models.PROTECT, null = True)

class Address(models.Model):
    '''
        Address model
    '''
    public_area = models.CharField(max_length = 255)
    number = models.CharField(max_length = 10)
    neighborhood = models.CharField(max_length = 255)
    municipality = models.CharField(max_length = 255)
    state = models.CharField(max_length = 30)
    postal_code = models.CharField(max_length = 10)

class Professor(models.Model):
    '''
        Professor of a campus
    '''
    name = models.CharField(max_length = 255)
    active = models.BooleanField()
    regular = models.BooleanField() # Efetivo
    exclusive = models.BooleanField() # Dedicação exclusiva
    employment_bond = models.ForeignKey('EmploymentBond', on_delete=models.PROTECT, null = True)
    title = models.ForeignKey('Title', on_delete=models.PROTECT, null = True)
    knowledge_area = models.ManyToManyField(KnowledgeArea)
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null = True)
    campus = models.ForeignKey('Campus', on_delete=models.PROTECT, null = True)
    contract = models.ForeignKey('Contract', on_delete=models.PROTECT, null = True)

class EmplymentBond(models.Model):
    workload = models.SmallIntegerField()

class Title(models.Model):
    name = models.CharField(max_length = 100)

class KnowledgeArea(models.Model):
    name = models.CharField(100)

class Contract(models.Model):
    beginning = models.DateField()
    end = models.DateField()

class Assignment(models.Model):
    '''
        Professors' current commitments
    '''
    professor = models.ForeignKey('Professor', on_delete=models.PROTECT, null = True)
    discipline = models.ForeignKey('Discipline', on_delete=models.PROTECT, null = True)
    period = models.ForeignKey('Period', on_delete=models.PROTECT, null = True)

class Period(models.Model):
    description = models.TextField()
    beginning = models.DateField()
    end = models.DateField()

class Course(models.Model):
    '''
        Course of a campus
    '''
    code = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 255)
    short_name = models.CharField(max_length = 30)
    coordinator = models.ForeignKey('Professor', on_delete=models.PROTECT, null = True)
    course_curriculum = models.ForeignKey('CourseCurriculum', on_delete=models.PROTECT, null = True)
    campus = models.ForeignKey('Campus', on_delete = models.PROTECT, null = True)

class Discipline(models.Model):
    '''
        Discipline of a course
    '''
    code = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 255)
    short_name = models.CharField(max_lenth = 255)
    summary = models.TextField() # Ementa
    workload = models.SmallIntegerField()
    block = models.SmallIntegerField()
    professor = models.ForeignKey('Professor', on_delete=models.PROTECT, null = True)
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null = True)
    course_curriculum = models.ForeignKey('CourseCurriculum', on_delete=models.PROTECT, null = True)

class CourseCurriculum(models.Model):
    '''
        Course curriculum of a course
    '''
    code = models.IntegerField(primary_key = True)
    active = models.BooleanField()
    starting_period = models.ForeignKey('Period', on_delete=models.PROTECT, null = True)
    ending_period = models.ForeignKey('Period', on_delete=models.PROTECT, null = True)
