from django.db import models


class nacionalidad(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True, verbose_name="Nombre")


    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='nacionalidad'
       verbose_name= 'nacionalidad'
       verbose_name_plural= 'nacionalidades'
       ordering = ['id']



class estadocivil(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True, verbose_name="Nombre")


    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='estadocivil'
       verbose_name= 'estadocivil'
       verbose_name_plural= 'estadosciviles'
       ordering = ['id']       


class genero(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True, verbose_name="Nombre")


    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='genero'
       verbose_name= 'genero'
       verbose_name_plural= 'generos'
       ordering = ['id']       



class miembro(models.Model):
    nombre = models.CharField(max_length=50, null=False,  verbose_name="Nombre")
    apellido = models.CharField(max_length=50, null=False,  verbose_name="Apellido")
    edad = models.CharField(max_length=10, null=False, default=0, verbose_name="Edad")
    di = models.CharField(max_length=50, null=False, verbose_name="Di")
    direccion = models.CharField(max_length=50, null=False,  verbose_name="Direccion")
    telefono = models.CharField(max_length=50, null=False,  verbose_name="Telefono")
    correo = models.EmailField(max_length=50, null=False,  verbose_name="Correo")
    nohijos = models.CharField(max_length=50, null=False,  verbose_name="Nohijos")
    nacionalidad = models.ForeignKey(nacionalidad, on_delete=models.CASCADE)
    estadocivil = models.ForeignKey(estadocivil, on_delete=models.CASCADE)
    genero = models.ForeignKey(genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
       db_table ='miembro'
       verbose_name= 'miembro'
       verbose_name_plural= 'miembros'
       ordering = ['-id']      




