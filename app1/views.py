from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def String(request):
    return HttpResponse('<marquee><i><h1> Hello!! GOOD MORNING </h1></i></marquee>')
