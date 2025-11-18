from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator



class Refugio(models.Model):
    nombre = models.CharField(max_length=100, null=True)

class Centro(models.Model):
    refugio = models.OneToOneField(Refugio, related_name='centro', on_delete = models.CASCADE)

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad_estimada = models.IntegerField() 
    centro = models.OneToOneField(Centro, related_name='animal', on_delete = models.CASCADE)

class Vacuna(models.Model):
    fabricante = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    animales = models.ManyToManyField(Animal, through='Animal_vacunas')

class Animal_vacunas(models.Model):
    id = models.IntegerField(primary_key=True) 
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete = models.CASCADE)

class Revision_veterinaria(models.Model):
    puntuacion_salud = models.IntegerField() 
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)

