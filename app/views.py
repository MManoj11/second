from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
    return HttpResponse('<marquee><h1>python is object oriented programming language</h1></marquee>')