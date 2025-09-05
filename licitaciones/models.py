from django.db import models

class Licitacion(models.Model):
    ESTADOS = [
        ("ABIERTO", "Abierto"),
        ("CERRADO", "Cerrado"),
        ("CANCELADO", "Cancelado"),
    ]

    nombre = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    proveedor = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
