from django.shortcuts import render


def prueba(request):

    return render(request, 'index.html')

def inicio(request):

    return render(request, 'inicio.html')


