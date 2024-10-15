from django.db import models

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    monedero = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Campo para el saldo

    def __str__(self):
        return self.name

