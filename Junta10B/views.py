from django.shortcuts import render


def inicio(request):

    return render(request, 'inicio.html')

def seguridad(request):

    return render(request, 'seguridad.html')

def datos_utiles(request):

    return render(request, 'datosUtiles.html')

def reciclaje(request):

    return render(request, 'reciclaje.html')
