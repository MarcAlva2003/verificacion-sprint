from django.db import models
from django import forms
from django.utils import timezone
from asyncio.windows_events import NULL

# Create your models here.

class prestamos(models.Model):

        loan_approved_date=models.DateField(auto_now=True)
        loan_month=models.IntegerField(default=1)
        loan_total=models.FloatField(default=0)
        loanType=models.TextField(max_length=40, default='Personales')
        id_cliente=models.IntegerField(default=1)
        id_sucursal=models.IntegerField(default=1)

        class Meta:
            ordering = ("-loan_approved_date",)
            verbose_name = "Prestamo"
            verbose_name_plural = "Prestamos"

        # def __str__(self):
        #     return self.loan_total,self.loan_approved_date