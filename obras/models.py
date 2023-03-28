from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Obra(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    #imagen = models.ImageField()
    autor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="autor" )

    def __str__(self):
        return f"{self.id} - {self.titulo}"


