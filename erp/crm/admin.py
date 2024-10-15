from django.contrib import admin
from .models import Client,Venta

class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'name', 'phone', 'monedero')  # Añadir monedero a la vista de lista

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id','cliente','tipo','monto','fecha_creacion')  # Añadir monedero a la vista de lista

admin.site.register(Client, ClientAdmin)
admin.site.register(Venta, VentaAdmin)

