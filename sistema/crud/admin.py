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
    list_display = ('name', 'add_city', 'phone1', 'email')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CourseGridAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class ContractTypeAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name',)
    
class ActivityNatureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('teacher',)
    
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('offer',)
    

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

