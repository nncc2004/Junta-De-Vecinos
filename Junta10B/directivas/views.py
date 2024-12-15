from django.shortcuts import render
from django.db.models import Max
from .models import Directivas, Cargos

def nosotros(request):

    max_anio_fin = Directivas.objects.aggregate(Max('anio_fin'))['anio_fin__max']
    directiva_mayor_anio = Directivas.objects.filter(anio_fin=max_anio_fin).first()

    if directiva_mayor_anio:
        cargos_mayor = Cargos.objects.filter(id_directiva=directiva_mayor_anio.id)
    else:
        cargos_mayor = []


    directivas = Directivas.objects.prefetch_related('cargos_set').order_by('-anio_fin')

    return render(request, 'nosotros.html', {
        'directiva_mayor': directiva_mayor_anio,
        'cargos_mayor': cargos_mayor,
        'directivas': directivas,
    })