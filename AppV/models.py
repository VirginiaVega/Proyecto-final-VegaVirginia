from django.db import models

# Create your models here.
class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=1000)
    cuerpo = models.CharField(max_length=5000)
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='entradas/', null=True, blank=True)
