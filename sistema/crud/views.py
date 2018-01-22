# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from crud.forms import CampusForm

def create_campus(request):
    context = {}
    if request.method == 'POST':
        form = CampusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CampusForm()

    context = {'form': form}

    return render(request, 'campus/create.html', {'form':form})
