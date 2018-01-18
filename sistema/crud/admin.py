# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
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

class CampusAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'short_name', 'add_city', 'phone1', 'email', 'active', )

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'campus', 'active', )

class CourseGridAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'date_ini', 'date_term', 'active',)
    
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'grid', 'area', 'ementa', 'block', 'work_load',)
    
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'wk_teaching', 'wk_resext', 'wk_compl', 'active',)
    
class ActivityNatureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'wk_week', 'wk_limit', 'nature',)
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'title', 'contract_type', 'phone1', 'phone2', 'email', 'active', 'efetivo',)
   
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'act_type', 'quantity', 'date_ini', 'date_term', 'observations',)

class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_ini', 'date_term',)
    
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'course', 'date_ini', 'date_term',)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('offer', 'discipline', 'teacher',)
    

admin.site.register(Campus,CampusAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(CourseGrid,CourseGridAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Discipline,DisciplineAdmin)
admin.site.register(Title,TitleAdmin)
admin.site.register(ContractType,ContractTypeAdmin)
admin.site.register(ActivityNature,ActivityNatureAdmin)
admin.site.register(ActivityType,ActivityTypeAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Semester,SemesterAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(Enrollment,EnrollmentAdmin)

