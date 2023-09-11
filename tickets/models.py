from django.db import models
import uuid
# Create your models here.

class especialidadTI(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name = 'ID especialidad')
    nombre = models.CharField(verbose_name='Nombre', max_length=100)

    def __str__(self):
        return self.nombre

class soporteTI(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True,)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    especialidad = models.ManyToManyField(especialidadTI, verbose_name='Especialidad')

    def __str__(self):
        return self.nombre

class tickets(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    titulo = models.CharField(max_length=500, verbose_name= 'Titulo')
    descripcion = models.TextField(verbose_name = 'descripcion' )
    soporte = models.ForeignKey(soporteTI,on_delete=models.CASCADE, max_length=500,  null=True, blank=True, verbose_name='soporte')

    def __str__(self):
        return self.titulo


