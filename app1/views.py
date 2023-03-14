from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('<h1>the best finisher</h1>')

def abd(request):
    return HttpResponse('<marquee><h1>MR.360....</h1></marquee>')