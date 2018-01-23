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
    ordering = ('short_name', )
    list_display = ('short_name', 'add_city', 'phone1', 'email', 'active', )
    search_fields = ['name', 'short_name', 'add_city']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'short_name', 'campus', 'active', )
    search_fields = ['name', 'short_name', 'campus__name', ]

@admin.register(CourseGrid)
class CourseGridAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'course', 'date_ini', 'date_term', 'active', )
    search_fields = ['name', 'course__name']

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', )
    search_fields = ['name', ]

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    ordering = ('short_name', )
    list_display = ('short_name', 'grid', 'area', 'block', 'work_load', )
    search_fields = ['name', 'short_name', 'area__name', 'block', ]

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', )
    search_fields = ['name', ]

@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'wk_teaching', 'wk_resext', 'wk_compl', 'active', )
    search_fields = ['name', ]

@admin.register(ActivityNature)
class ActivityNatureAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', )
    search_fields = ['name', ]

@admin.register(ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'wk_week', 'wk_limit', 'nature', )
    search_fields = ['name', ]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'course', 'title', 'efetivo', 'active', )
    filter_horizontal = ('area','activity', )
    search_fields = ['name', 'course__name', 'title__name', ]

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    ordering = ('date_ini', )
    list_display = ('short_name', 'act_type', 'date_ini', 'date_term', )
    search_fields = ['short_name', 'act_type__name', ]

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'date_ini', 'date_term', )
    search_fields = ['name', ]

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'semester', 'course', 'date_ini', 'date_term', )
    search_fields = ['name', 'course__name']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    ordering = ('offer', )
    list_display = ('offer', 'discipline', 'teacher', )
    search_fields = ['discipline__name', 'teacher__name']
