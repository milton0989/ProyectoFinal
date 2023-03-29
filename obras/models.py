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

class Perfil(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="perfil")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True)
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")
