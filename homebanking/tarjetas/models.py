from tkinter import CASCADE
from django.db import models

# Create your models here.

class Project(models.Model):    #Hereda de Django para obtener funcionalidad que yo necesito
    tittle = models.CharField(max_length=200,verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True)
    link =models.URLField(null=True,blank=True,verbose_name='Enlace Web')
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")
    owner = models.ForeignKey('auth.user', related_name='posts', on_delete= models.CASCADE)

class Tarjetas(models.Model):
    numero_tarjeta = models.IntegerField()
    cvv = models.IntegerField()
    fecha_emision = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    tipo_tarjeta = models.TextField(max_length=20)
    marca_tarjeta = models.TextField(max_length=20)
    account_id = models.IntegerField()
    customer_id = models.IntegerField()

class Meta:
    ordering = ("-customer_id",)
    verbose_name = "Tarjeta"
    verbose_name_plural = "Tarjetas"

def __str__(self):
    return self.title