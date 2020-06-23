from django.shortcuts import render

from .models import Reference

# Create your views here.
def index(request):
    entries = Reference.objects.order_by('-date')
    return render(request, 'references/index.html', {'entries':entries})

def entry_1(request):
    entry = Reference.objects.get(pk=1)
    return render(request, 'references/entry_1.html', {'entry':entry})

def entry_2(request):
    entry = Reference.objects.get(pk=2)
    return render(request, 'references/entry_2.html', {'entry':entry})
