from django.db import models

# Create your models here.
class amigos(models.Model):
    
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    edad = models.IntegerField()
    cumpleaños = models.DateField()