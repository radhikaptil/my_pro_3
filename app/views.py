from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Shital(request):
    return HttpResponse('<marquee><h1> Hey!! Have a nice day </h1></marquee>')
