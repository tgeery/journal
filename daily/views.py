from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'daily/index.html', {})

def entry_1(request):
    return render(request, 'daily/entry_1.html', {})

def entry_2(request):
    return render(request, 'daily/entry_2.html', {})
