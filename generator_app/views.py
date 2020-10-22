from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return HttpResponse("HELLO WORLD")


def index(request):
    return render(request, 'generator_app/home.html')

def about(request):
    return render(request, 'generator_app/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLMNOPQSTUVWXYZ')
    numbers = list('0123456789')
    special = list('!@#$%^&*_')
    length = int(request.GET.get('length'))
    the_password = ''

    if request.GET.get('uppercase'):
        characters.extend(uppercase)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('special'):
        characters.extend(special)

    for i in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator_app/password.html', {'password': the_password})
