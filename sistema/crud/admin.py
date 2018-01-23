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

# Some inline definitions for the admin
class CourseInline(admin.TabularInline):
    model = Course
    show_change_link = True
    extra = 0

class DisciplineInline(admin.TabularInline):
    model = Discipline
    show_change_link = True
    extra = 0

class TeacherInline(admin.TabularInline):
    model = Teacher
    show_change_link = True
    extra = 0

class ActivityInline(admin.TabularInline):
    model = Activity
    show_change_link = True
    extra = 0

class ActivityTypeInline(admin.TabularInline):
    model = Activity
    show_change_link = True
    extra = 0

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    show_change_link = True
    extra = 0

class OfferInline(admin.TabularInline):
    model = Offer
    show_change_link = True
    extra = 0

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    ordering = ('short_name',)
    list_display = ('short_name', 'add_city', 'phone1', 'email', 'active', )
    inlines = [CourseInline,]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'short_name', 'campus', 'active', )
    inlines = [TeacherInline,]

@admin.register(CourseGrid)
class CourseGridAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'course', 'date_ini', 'date_term', 'active',)
    inlines = [DisciplineInline,]

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name',)
    inlines = [DisciplineInline,]

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    ordering = ('short_name',)
    list_display = ('short_name', 'grid', 'area', 'block', 'work_load',)

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name',)
    inlines = [TeacherInline,]

@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'wk_teaching', 'wk_resext', 'wk_compl', 'active',)
    inlines = [TeacherInline,]

@admin.register(ActivityNature)
class ActivityNatureAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name',)

@admin.register(ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'wk_week', 'wk_limit', 'nature',)
    inlines = [ActivityInline,]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'course', 'title', 'efetivo', 'active')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    ordering = ('date_ini',)
    list_display = ('short_name', 'act_type', 'date_ini', 'date_term',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'date_ini', 'date_term',)
    inlines = [OfferInline,]

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'semester', 'course', 'date_ini', 'date_term',)
    inlines = [EnrollmentInline,]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    ordering = ('offer',)
    list_display = ('offer', 'discipline', 'teacher',)
