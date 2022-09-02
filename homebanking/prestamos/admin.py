from django.contrib import admin
from .models import prestamos

# Register your models here.
class PrestamosAdmin (admin.ModelAdmin):
    readonly_fields= ('fecha_vencimiento')
    admin.site.register(prestamos)
