from django.db import models

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    monedero = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)  # Relación con el modelo Client
    tipo = models.CharField(max_length=100)  # Tipo de venta (puedes definir las opciones que necesites)
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Monto de la venta
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return f"Venta {self.id} - {self.cliente.name} - {self.tipo}"

