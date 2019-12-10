from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Journal

def index(request):
    entries = Journal.objects.order_by('-date')
    return render(request, 'daily/index.html', {'entries':entries})

def entry_1(request):
    entry = Journal.objects.get(pk=1)
    return render(request, 'daily/entry_1.html', {'entry':entry})

def entry_2(request):
    entry = Journal.objects.get(pk=2)
    return render(request, 'daily/entry_2.html', {'entry':entry})

def entry_3(request):
    entry = Journal.objects.get(pk=3)
    return render(request, 'daily/entry_3.html', {'entry':entry})

def entry_4(request):
    entry = Journal.objects.get(pk=4)
    return render(request, 'daily/entry_4.html', {'entry':entry})

def entry_5(request):
    entry = Journal.objects.get(pk=5)
    return render(request, 'daily/entry_5.html', {'entry':entry})

def entry_6(request):
    entry = Journal.objects.get(pk=6)
    return render(request, 'daily/entry_6.html', {'entry':entry})

def entry_7(request):
    entry = Journal.objects.get(pk=7)
    return render(request, 'daily/entry_7.html', {'entry':entry})
