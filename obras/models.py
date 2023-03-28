from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Obra(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="obras", null=True, blank=True)
    autor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="autor" )

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''


    def __str__(self):
        return f"{self.id} - {self.titulo}"


