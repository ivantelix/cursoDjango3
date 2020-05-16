from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre Persona")    
    apellido = models.CharField(max_length=100, null=True, blank=True)
    dni = models.CharField(max_length=8, unique=True)


class Familia(models.Model):
    PARENTESCOS_CHOICES = [
        ('padre', 'Padre'),
        ('hermano', 'Hermano/a'),
        ('madre', 'Madre'),
        ('hijo', 'Hijo/a'),
        ('esposo', 'Esposo/a'),
    ]

    nombre = models.CharField(max_length=100, null=True, blank=True)
    parentesco = models.CharField(max_length=50, null=True, blank=True, choices=PARENTESCOS_CHOICES)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE,  default='1')