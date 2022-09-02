from django.db import models

# Create your models here.

# class Project(models.Model):    #Hereda de Django para obtener funcionalidad que yo necesito
#     tittle = models.CharField(max_length=200,verbose_name="Titulo")
#     description = models.TextField(verbose_name="Descripcion")
#     image = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True)
#     link =models.URLField(null=True,blank=True,verbose_name='Enlace Web')
#     created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
#     updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")

    # class Meta:
    #     verbose_name = "proyecto"
    #     verbose_name_plural = "proyectos"
    #     ordering = ["-created"]

    # def __str__(self) -> str:
    #     return self.tittle

class cuenta(models.Model):
        balance=models.IntegerField(default=0)
        iban=models.TextField(max_length=24)
        tipo_de_cuenta=models.TextField(max_length=20, null=True)
        customer_id=models.IntegerField(null=True)
        user_email=models.EmailField(max_length=254, null=True)

        def __repr__(self):
                return f'saldo: {self.balance}, id_cliente: {self.account_id}'

class movimientos(models.Model):
        iban=models.TextField(max_length=100)
        monto=models.IntegerField()
        tipo_operacion=models.TextField(max_length=200)
        hora=models.DateTimeField()
