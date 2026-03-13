from django.shortcuts import render # render, sere para rendeizar o html de outro lugar/pasta template == render <= template/algumacoisa.html
from django.http import HttpResponse # Serve para escrver html

# Create your views here.

def my_home1(request):
    print('Minha home')
    return HttpResponse('estou na home http')

def my_home(request):
    print('home render')
    return render(request, 'home/index.html')