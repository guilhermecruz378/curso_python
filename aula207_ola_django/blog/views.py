from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def my_blog(request):
#     print('Blog')
#     return HttpResponse('Meu blog')

# def exemplo(request):
#     print('Exemplo de aninhar urls')
#     return HttpResponse('Exemplo de aninhar urls')

def my_blog(request):
    print('Blog')
    return render(request, 'blog/index.html')

def exemplo(request):
    print('Exemplo de aninhar urls')
    return render(request, 'blog/Exemplo.html')