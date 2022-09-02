from django.contrib import admin

# Register your models here.

from .models import cuenta

class CuentaAdmin (admin.ModelAdmin):
    readonly_fields= ('id')
    admin.site.register(cuenta)
# admin.site.register(cuenta)