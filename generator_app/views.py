from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(response):
    return HttpResponse("HELLO WORLD")


def index(response):
    return render(response, 'generator_app/home.html')
