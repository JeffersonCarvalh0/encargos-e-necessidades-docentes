# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.admin import AdminSite
from crud.models import (
    Campus,
    Course,
    CourseGrid,
    Area,
    Discipline,
    Title,
    ContractType,
    ActivityNature,
    ActivityType,
    Teacher,
    Activity,
    Semester,
    Offer,
    Enrollment,
)

AdminSite.site_header = 'Controle de Encargos Docentes'
AdminSite.index_title = 'UESPI'
AdminSite.site_title = 'Controle de Encargos Docentes'
AdminSite.site_url = None

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('short_name', 'add_city', 'phone1', 'email', 'active', )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'campus', 'active', )

@admin.register(CourseGrid)
class CourseGridAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'date_ini', 'date_term', 'active',)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'grid', 'area', 'block', 'work_load',)

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'wk_teaching', 'wk_resext', 'wk_compl', 'active',)

@admin.register(ActivityNature)
class ActivityNatureAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'wk_week', 'wk_limit', 'nature',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'title', 'active', 'efetivo',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'act_type', 'date_ini', 'date_term',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_ini', 'date_term',)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'course', 'date_ini', 'date_term',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('offer', 'discipline', 'teacher',)
