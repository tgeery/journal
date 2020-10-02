from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Journal

def index(request):
    entries = Journal.objects.order_by('-date')
    return render(request, 'daily/index.html', {"entries":entries,"titles":[{"name":"test"},{"name":"test2"}]})

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

def entry_8(request):
    entry = Journal.objects.get(pk=8)
    return render(request, 'daily/entry_8.html', {'entry':entry})

def entry_9(request):
    entry = Journal.objects.get(pk=9)
    return render(request, 'daily/entry_9.html', {'entry':entry})

def entry_10(request):
    entry = Journal.objects.get(pk=10)
    return render(request, 'daily/entry_10.html', {'entry':entry})

def entry_11(request):
    entry = Journal.objects.get(pk=11)
    return render(request, 'daily/entry_11.html', {'entry':entry})

def entry_12(request):
    entry = Journal.objects.get(pk=12)
    return render(request, 'daily/entry_12.html', {'entry':entry})

def entry_13(request):
    entry = Journal.objects.get(pk=13)
    return render(request, 'daily/entry_13.html', {'entry':entry})

def entry_14(request):
    entry = Journal.objects.get(pk=14)
    return render(request, 'daily/entry_14.html', {'entry':entry})

def entry_15(request):
    entry = Journal.objects.get(pk=15)
    return render(request, 'daily/entry_15.html', {'entry':entry})

def entry_16(request):
    entry = Journal.objects.get(pk=16)
    return render(request, 'daily/entry_16.html', {'entry':entry})

def entry_17(request):
    entry = Journal.objects.get(pk=17)
    return render(request, 'daily/entry_17.html', {'entry':entry})

def entry_18(request):
    entry = Journal.objects.get(pk=18)
    return render(request, 'daily/entry_18.html', {'entry':entry})

def entry_19(request):
    entry = Journal.objects.get(pk=19)
    return render(request, 'daily/entry_19.html', {'entry':entry})

def entry_20(request):
    entry = Journal.objects.get(pk=20)
    return render(request, 'daily/entry_20.html', {'entry':entry})

def entry_21(request):
    entry = Journal.objects.get(pk=21)
    return render(request, 'daily/entry_21.html', {'entry':entry})

def entry_22(request):
    entry = Journal.objects.get(pk=22)
    return render(request, 'daily/entry_22.html', {'entry':entry})

def entry_23(request):
    entry = Journal.objects.get(pk=23)
    return render(request, 'daily/entry_23.html', {'entry':entry})

def entry_24(request):
    entry = Journal.objects.get(pk=24)
    return render(request, 'daily/entry_24.html', {'entry':entry})

def entry_25(request):
    entry = Journal.objects.get(pk=25)
    return render(request, 'daily/entry_25.html', {'entry':entry})

def entry_26(request):
    entry = Journal.objects.get(pk=26)
    return render(request, 'daily/entry_26.html', {'entry':entry})

def entry_27(request):
    entry = Journal.objects.get(pk=27)
    return render(request, 'daily/entry_27.html', {'entry':entry})

def entry_28(request):
    entry = Journal.objects.get(pk=28)
    return render(request, 'daily/entry_28.html', {'entry':entry})

def entry_29(request):
    entry = Journal.objects.get(pk=29)
    return render(request, 'daily/entry_29.html', {'entry':entry})

def entry_30(request):
    entry = Journal.objects.get(pk=30)
    return render(request, 'daily/entry_30.html', {'entry':entry})

def entry_31(request):
    entry = Journal.objects.get(pk=31)
    return render(request, 'daily/entry_31.html', {'entry':entry})

def entry_32(request):
    entry = Journal.objects.get(pk=32)
    return render(request, 'daily/entry_32.html', {'entry':entry})

def entry_33(request):
    entry = Journal.objects.get(pk=33)
    return render(request, 'daily/entry_33.html', {'entry':entry})

def entry_34(request):
    entry = Journal.objects.get(pk=34)
    return render(request, 'daily/entry_34.html', {'entry':entry})

def entry_35(request):
    entry = Journal.objects.get(pk=35)
    return render(request, 'daily/entry_35.html', {'entry':entry})

def entry_36(request):
    entry = Journal.objects.get(pk=36)
    return render(request, 'daily/entry_36.html', {'entry':entry})

def entry_37(request):
    entry = Journal.objects.get(pk=37)
    return render(request, 'daily/entry_37.html', {'entry':entry})

def entry_38(request):
    entry = Journal.objects.get(pk=38)
    return render(request, 'daily/entry_38.html', {'entry':entry})

def entry_39(request):
    entry = Journal.objects.get(pk=39)
    return render(request, 'daily/entry_39.html', {'entry':entry})

def entry_40(request):
    entry = Journal.objects.get(pk=40)
    return render(request, 'daily/entry_40.html', {'entry':entry})

def entry_41(request):
    entry = Journal.objects.get(pk=41)
    return render(request, 'daily/entry_41.html', {'entry':entry})

def entry_42(request):
    entry = Journal.objects.get(pk=42)
    return render(request, 'daily/entry_42.html', {'entry':entry})

def entry_43(request):
    entry = Journal.objects.get(pk=43)
    return render(request, 'daily/entry_43.html', {'entry':entry})

def entry_44(request):
    entry = Journal.objects.get(pk=44)
    return render(request, 'daily/entry_44.html', {'entry':entry})

def entry_45(request):
    entry = Journal.objects.get(pk=45)
    return render(request, 'daily/entry_45.html', {'entry':entry})

def entry_46(request):
    entry = Journal.objects.get(pk=46)
    return render(request, 'daily/entry_46.html', {'entry':entry})

def entry_47(request):
    entry = Journal.objects.get(pk=47)
    return render(request, 'daily/entry_47.html', {'entry':entry})

def entry_48(request):
    entry = Journal.objects.get(pk=48)
    return render(request, 'daily/entry_48.html', {'entry':entry})

def entry_49(request):
    entry = Journal.objects.get(pk=49)
    return render(request, 'daily/entry_49.html', {'entry':entry})

def entry_50(request):
    entry = Journal.objects.get(pk=50)
    return render(request, 'daily/entry_50.html', {'entry':entry})

def entry_51(request):
    entry = Journal.objects.get(pk=51)
    return render(request, 'daily/entry_51.html', {'entry':entry})
