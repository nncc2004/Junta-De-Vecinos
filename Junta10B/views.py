from django.http import HttpResponse
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render


def prueba(request):

    return render(request, 'index.html')

def inicio(request):

    return render(request, 'inicio.html')
