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
    addr_street = models.CharField(max_length = 100)
    addr_no = models.CharField(max_length = 5)
    addr_neighbor = models.CharField(max_length = 100)
    addr_city = models.CharField(max_length = 100)
    addr_uf = models.CharField(max_length = 50)
    addr_zip = models.CharField(max_length = 10)
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()
    email = models.EmailField()
    site = models.URLField()
    active = mdoels.BooleanField()

class Teacher(models.Model):
    '''
        Teacher of a campus
    '''
    cpf = models.CharField(max_length = 11)
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()
    active = models.BooleanField()
    effective = models.BooleanField()
    contract_term = models.DateField()
    area = models.ManyToManyField(Area)
    title = models.ForeignKey('Title', on_delete=models.PROTECT, null = True)
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null = True)
    contract = models.ForeignKey('Contract', on_delete=models.PROTECT, null = True)

class Course(models.Model):
    '''
    Course of a campus
    '''
    name = models.CharField(max_length = 255)
    short_name = models.CharField(max_length = 30)
    active = models.BooleanField
    campus = models.ForeignKey('Campus', on_delete = models.PROTECT, null = True)

class Discipline(models.Model):
    '''
    Discipline of a course
    '''
    name = models.CharField(max_length = 255)
    short_name = models.CharField(max_lenth = 255)
    ementa = models.TextField() # Ementa
    block = models.SmallIntegerField()
    workload = models.SmallIntegerField()
    active = models.BooleanField()
    area = models.ForeignKey('Area', on_delete=models.PROTECT, null = True)
    course_grid = models.ForeignKey('CourseGrid', on_delete=models.PROTECT, null = True)

class CourseGrid(models.Model):
    '''
    Course curriculum of a course
    '''
    active = models.BooleanField()
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null = True)
    date_ini = models.DateField()
    date_term = models.DateField()
    active = models.BooleanField()

class Activity(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT, null = True)
    actv_type = models.ForeignKey('ActivityType', on_delete=models.PROTECT, null = True)
    quantity = models.IntegerField()
    date_ini = models.DateField()
    date_term = models.DateField()
    comment = models.TextField()

class ActivityType(models.Model):
    name = models.CharField(max_length = 255)
    wl_week = models.SmallIntegerField()
    wl_max = models.SmallIntegerField()
    actv_type = models.SmallIntegerField()
    comment = models.TextField()
    active = models.BooleanField()

class Title(models.Model):
    name = models.CharField(max_length = 100)

class Area(models.Model):
    name = models.CharField(100)

class ContractType(models.Model):
    name = models.CharField(max_length = 255)
    wl_teaching = models.SmallIntegerField()
    wl_extres = models.SmallIntegerField()
    active = models.BooleanField()

# class Assignment(models.Model):
#     '''
#         Professors' current commitments
#     '''
#     professor = models.ForeignKey('Professor', on_delete=models.PROTECT, null = True)
#     discipline = models.ForeignKey('Discipline', on_delete=models.PROTECT, null = True)
#     period = models.ForeignKey('Period', on_delete=models.PROTECT, null = True)
#
# class Period(models.Model):
#     description = models.TextField()
#     beginning = models.DateField()
#     end = models.DateField()


# class SysUser(auth.User):
#     campus = models.ForeignKey('Campus', on_delete=models.PROTECT, null = none)
#     user = models.OneToOneField(auth.User)
