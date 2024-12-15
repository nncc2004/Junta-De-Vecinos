from django.contrib import admin
from .models import Directivas, Cargos

class CargosAdmin(admin.ModelAdmin):
    # Mostrar el nombre de la directiva (el valor calculado) en lugar del id_directiva
    list_display = ('nombre', 'cargo', 'id_directiva')

    # Usar el campo 'nombre' de Directivas para mostrarlo como opción en el campo id_directiva
    def id_directiva(self, obj):
        return obj.id_directiva.nombre
    id_directiva.short_description = 'Directiva'  # Nombre personalizado de la columna


admin.site.register(Directivas)
admin.site.register(Cargos)
