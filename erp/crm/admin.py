from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'name', 'phone', 'monedero')  # Añadir monedero a la vista de lista

admin.site.register(Client, ClientAdmin)

