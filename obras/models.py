from django.db import models

# Create your models here.

class Obra(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField()
    autor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.titulo}"


