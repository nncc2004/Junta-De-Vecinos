from django.db import models

class Directivas(models.Model):
    anio_inicio = models.IntegerField()
    anio_fin = models.IntegerField()
    nombre = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Asigna el valor de 'nombre' antes de guardar el objeto
        self.nombre = f"{self.anio_inicio} - {self.anio_fin}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.anio_inicio} - {self.anio_fin}"
    
    

class Cargos(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    id_directiva = models.ForeignKey(Directivas, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"
