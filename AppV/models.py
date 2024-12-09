from django.db import models

# Create your models here.
class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=255)
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    
