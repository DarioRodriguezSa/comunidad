from django.db import models

class estate(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name="Nombre")


    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='estate'
       verbose_name= 'estate'
       verbose_name_plural= 'estates'
       ordering = ['id']        
                  



class tipo(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name="Nombre")


    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='tipo'
       verbose_name= 'tipo'
       verbose_name_plural= 'tipos'
       ordering = ['id']        
                  


class evento(models.Model):
     titulo = models.CharField(max_length=100, null=False, verbose_name="Titulo")
     invitante=models.CharField(max_length=100, null=False, verbose_name="Invitante")
     fecha = models.DateField(max_length=25)
     encargado = models.CharField(max_length=75, null=False, verbose_name="Encargado")
     staff = models.CharField(max_length=100, null=False, verbose_name="Staff")
     lugar = models.CharField(max_length=100, null=False, verbose_name="Lugar")
     noasistentes = models.IntegerField( null=False, verbose_name="Noasistentes")
     estate = models.ForeignKey(estate, on_delete=models.CASCADE)
     tipo = models.ForeignKey(tipo, on_delete=models.CASCADE)

     def __str__(self):
        return self.nombre
    
     class Meta:
       db_table ='evento'
       verbose_name= 'evento'
       verbose_name_plural= 'eventos'
       ordering = ['-id']  