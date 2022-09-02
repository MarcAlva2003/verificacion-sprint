from Clientes.models import clientes
from django.contrib import admin
# Create your models here.
class ClienteAdmin (admin.ModelAdmin):
    readonly_fields = ('created-at','updated-at')
    admin.site.register(clientes)

    def __str__(self):
        return self.nombre