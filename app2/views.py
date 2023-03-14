from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse('<h1>The Best Batsman</h1>')

def raina(request):
    return HttpResponse('<marquee><h1>MR.IPL</h1></marquee>')