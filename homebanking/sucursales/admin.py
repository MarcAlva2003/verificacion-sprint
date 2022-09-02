from django.contrib import admin
from sucursales.models import Sucursal
# Register your models here.

class SucursalAdmin (admin.ModelAdmin):
    readonly_fields= ('created-at','updated-at')
admin.site.register(Sucursal)
