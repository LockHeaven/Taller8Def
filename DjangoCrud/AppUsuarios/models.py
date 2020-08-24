from django.db import models
from django.forms import ModelForm, Textarea

class tipodocumento(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 150)

    def __str__(self):
        return '{}'.format(self.nombre)
    
class ciudad(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 150)

    def __str__(self):
        return '{}'.format(self.nombre)

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    documento = models.IntegerField()
    email = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 12)
    usuario = models.CharField(max_length = 15)
    password = models.CharField(max_length = 30)
    fechanacimiento = models.CharField(max_length = 30)
    edad = models.IntegerField()
    tipodocumento = models.ForeignKey(tipodocumento, on_delete = models.CASCADE)
    residencia = models.ForeignKey(ciudad, on_delete = models.CASCADE)

    

