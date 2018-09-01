from django.shortcuts import render

from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import json


# Create your views here.
def write_to_cache(request):
    key = 'hahaha'
    cache.set(key,json.dumps('qqqqqqqqq'),settings.NEVER_REDIS_TIMEOUT)

    return render(request,"test.html")

def read_from_cache(request):
    key = 'hahaha'
    value = cache.get(key)
    if value==None:
        data=None
    else:
        data = json.loads(value)
    return render(request,"test.html",{"show":data})

@cache_page(1000)
def abc(request):
    print("@@@@@@@@@@@@@@@@@@@@@@@@")
    return render(request,"test.html")



@cache_page(10)
def cde(request):
    print('#############')
    return render(request,"test.html")

def dfg(request):
    print('%%%%%%%%%%%%%')
    return render(request,"test.html")
