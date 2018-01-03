# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from crud.models import (
    CourseGrid,
    Activity,
    ActivityType,
    Title,
    ContractType,
    Campus,
    Area,
    Teacher,
    Course,
    Discipline,
)

admin.site.register(CourseGrid)
admin.site.register(Activity)
admin.site.register(ActivityType)
admin.site.register(Title)
admin.site.register(ContractType)
admin.site.register(Campus)
admin.site.register(Area)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Discipline)

