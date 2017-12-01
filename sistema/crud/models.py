# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Campus(models.Model):
    '''
        Campus of the institution
    '''
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)

class Professor(models.Model):
    '''
        Professor of a campus
    '''
    registry = models.CharField(primary_key = True, max_length = 7) # Not sure about the length
    name = models.CharField(max_length = 255)
    cpf = models.CharField(max_length = 11)
    employment_bond = models.CharField(max_length = 50)
    current_workload = models.SmallIntegerField()
    coordinator = models.BooleanField(default = False)
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null = True)
    campus = models.ForeignKey('Campus', on_delete=models.PROTECT, null = True)

class Course(models.Model):
    '''
        Course of a campus
    '''
    code = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 255)
    course_curriculum = models.ForeignKey('CourseCurriculum', on_delete=models.PROTECT, null = True)
    campus = models.ForeignKey('Campus', on_delete = models.PROTECT, null = True)

class Discipline(models.Model):
    '''
        Discipline of a course
    '''
    code = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 255)
    workload = models.SmallIntegerField()
    professor = models.ForeignKey('Professor', on_delete=models.PROTECT, null = True)
    offered = models.BooleanField(default = False)

class CourseCurriculum(models.Model):
    '''
        Course curriculum of a course
    '''
    code = models.IntegerField(primary_key = True)
    starting_semester = models.SmallIntegerField() # ex:20151 for 2015.1
    ending_semester = models.SmallIntegerField()
