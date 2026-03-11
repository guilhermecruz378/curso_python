from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_home(request):
    print('Minha home')
    return HttpResponse('estou na home')