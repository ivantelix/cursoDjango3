from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)    
    apellido = models.CharField(max_length=100, null=True, blank=True)
    dni = models.CharField(max_length=8, null=True, blank=True)