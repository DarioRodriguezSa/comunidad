from django.db import models
from eventos.models import evento

class gasto(models.Model):
     presupuesto = models.TextField( null=False, verbose_name="Presupuesto")
     transporte = models.TextField( null=False, verbose_name="Trasporte")
     personal = models.TextField( null=False,  verbose_name="Personal")
     combustible = models.TextField( null=False,  verbose_name="Combustible")
     alquiler = models.TextField( null=False,  verbose_name="Alquiler")
     viaticos = models.TextField( null=False,  verbose_name="Viaticos")
     donaciones = models.TextField( null=False,  verbose_name="Donaciones")
     otros = models.TextField(null=False,  verbose_name="Otros")
     totalgastado=models.TextField( null=False, verbose_name="Totalgastado")
     residuo = models.TextField( null=False, verbose_name="Residuo")
     eventoa = models.ForeignKey(evento, on_delete=models.CASCADE)

     def __str__(self):
        return self.nombre
    
     class Meta:
       db_table ='gasto'
       verbose_name= 'gasto'
       verbose_name_plural= 'gastos'
       ordering = ['-id']                 
