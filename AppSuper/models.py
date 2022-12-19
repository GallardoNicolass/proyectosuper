from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    legajo= models.IntegerField()

    def __str__(self):
        return self.nombre


class Gerente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    legajo=models.IntegerField()

    def __str__(self):
        return self.nombre



class encargado(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    sucursal= models.IntegerField()

    def __str__(self):
        return self.nombre
