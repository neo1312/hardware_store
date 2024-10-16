from django.db import models

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)  # ID único
    nombre = models.CharField(max_length=100)  # Nombre del proveedor
    numero = models.CharField(max_length=15)  # Número de contacto
    direccion = models.CharField(max_length=255)  # Dirección del proveedor

    def __str__(self):
        return self.nombre

