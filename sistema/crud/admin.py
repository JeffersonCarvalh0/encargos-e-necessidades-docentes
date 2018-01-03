# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from crud.models import (
    Campus,
    Area,
    Teacher,
    Course,
    Discipline,
)

admin.site.register(Campus)
admin.site.register(Area)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Discipline)
