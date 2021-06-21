from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Motivo(models.Model):
    idMotivo = models.IntegerField(primary_key=True, verbose_name='Id de Motivo')
    nombreMotivo = models.CharField(max_length=50, verbose_name='Nombre de Motivo')

    def __str__(self):
        return (self.nombreMotivo)

class Usuario(models.Model):
    NickUsuario = models.CharField(max_length=30, primary_key=True, verbose_name='Nick de Usuario')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.CharField(max_length=70, verbose_name='Mail')
    mensaje = models.CharField(max_length=200, verbose_name='Mensaje')
    idMotivo = models.ForeignKey(Motivo, on_delete=CASCADE)

    def __str__(self):
        return (self.NickUsuario)