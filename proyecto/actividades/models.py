from django.db import models 
from miembros.models import miembro, nacionalidad


class clase(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True, verbose_name="Nombre")
    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='clase'
       verbose_name= 'clase'
       verbose_name_plural= 'clases'
       ordering = ['id']

class categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True, verbose_name="Nombre")


    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='categoria'
       verbose_name= 'categoria'
       verbose_name_plural= 'categorias'
       ordering = ['id']

class curso(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True, verbose_name="Nombre")


    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='curso'
       verbose_name= 'curso'
       verbose_name_plural= 'cursos'
       ordering = ['id']      
       

class status(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True, verbose_name="Nombre")


    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='status'
       verbose_name= 'status'
       verbose_name_plural= 'statuses'
       ordering = ['id']

class maestro(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name="Nombre")


    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='maestro'
       verbose_name= 'maestro'
       verbose_name_plural= 'maestros'
       ordering = ['id']    



class tiempo(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name="Nombre")


    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='tiempo'
       verbose_name= 'tiempo'
       verbose_name_plural= 'tiempos'
       ordering = ['id']        
                  


class actividad(models.Model):
     fechainicio = models.DateField(max_length=25)
     fechafin = models.DateField(max_length=25)
     duracion = models.IntegerField(null=False, verbose_name="Duracion")
     miembroa = models.ForeignKey(miembro, on_delete=models.CASCADE, related_name='actividad_miembroa')
     maestro = models.ForeignKey(maestro, on_delete=models.CASCADE, related_name='actividad_maestro')
     clase = models.ForeignKey(clase, on_delete=models.CASCADE)
     status = models.ForeignKey(status, on_delete=models.CASCADE)
     curso = models.ForeignKey(curso, on_delete=models.CASCADE)
     tiempo = models.ForeignKey(tiempo, on_delete=models.CASCADE)
     categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)

     def __str__(self):
        return self.nombre
    
     class Meta:
       db_table ='actividad'
       verbose_name= 'actividad'
       verbose_name_plural= 'actividades'
       ordering = ['-id']    

class noactividad(models.Model):
     nombre = models.CharField(max_length=100, null=False,  verbose_name="Nombre")
     fechainicio = models.DateField(max_length=25)
     fechafin= models.DateField(max_length=25)
     nacionalidade = models.ForeignKey(nacionalidad, on_delete=models.CASCADE ,related_name='nacion')
     duracion = models.IntegerField(null=False, verbose_name="Duracion")
     maestro = models.ForeignKey(maestro, on_delete=models.CASCADE,related_name='maestro')
     curso = models.ForeignKey(curso, on_delete=models.CASCADE)
     edad = models.CharField(max_length=10, null=False, default=0, verbose_name="Edad")
     clase = models.ForeignKey(clase, on_delete=models.CASCADE)
     tiempo = models.ForeignKey(tiempo, on_delete=models.CASCADE)
     status = models.ForeignKey(status, on_delete=models.CASCADE)
     categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)

     def __str__(self):
        return self.nombre
    
     class Meta:
       db_table ='noactividad'
       verbose_name= 'noactividad'
       verbose_name_plural= 'noactividades'
       ordering = ['-id']     

class acta(models.Model):
     titulo = models.CharField(max_length=100, null=False,  verbose_name="Nombre")
     fecha = models.DateField(max_length=25)
     sheij = models.CharField(max_length=100, null=False,  verbose_name="Sheij")
     novio = models.CharField(max_length=100, null=False,  verbose_name="Novio")
     novia = models.CharField(max_length=100, null=False,  verbose_name="Novia")
     guardian = models.CharField(max_length=100, null=False,  verbose_name="Guardian")
     testigos = models.CharField(max_length=350, null=False,  verbose_name="Testigos")

     def __str__(self):
        return self.nombre
    
     class Meta:
       db_table ='acta'
       verbose_name= 'acta'
       verbose_name_plural= 'actas'
       ordering = ['-id']                 
