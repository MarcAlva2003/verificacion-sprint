from django.db import models

# Create your models here.
class Project(models.Model):    #Hereda de Django para obtener funcionalidad que yo necesito
        tittle = models.CharField(max_length=200,verbose_name="Titulo")
        description = models.TextField(verbose_name="Descripcion")
        image = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True)
        link =models.URLField(null=True,blank=True,verbose_name='Enlace Web')
        created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
        updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")
        from django.db import models

class empleado(models.Model):
        employee_name=models.TextField(max_length=100)
        employee_surname=models.TextField(max_length=100)
        employee_hire_date=models.TextField(max_length=300)
        employee_dni=models.TextField(max_length=100)
        branch_id=models.IntegerField()
        direccion_id=models.IntegerField()


class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
def __str__(self) -> str:
        return self.tittle