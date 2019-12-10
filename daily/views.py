from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Journal

def index(request):
    entries = Journal.objects.order_by('-date')
    return render(request, 'daily/index.html', {'entries':entries})

def entry_1(request):
    return render(request, 'daily/entry_1.html', {})

def entry_2(request):
    return render(request, 'daily/entry_2.html', {})

def entry_3(request):
    return render(request, 'daily/entry_3.html', {})

def entry_4(request):
    return render(request, 'daily/entry_4.html', {})

def entry_5(request):
    return render(request, 'daily/entry_5.html', {})

def entry_6(request):
    return render(request, 'daily/entry_6.html', {})

def entry_7(request):
    return render(request, 'daily/entry_7.html', {})
