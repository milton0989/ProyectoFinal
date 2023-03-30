from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Obra(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Obra')
    subtitulo = models.CharField(max_length=50, verbose_name='Ubicación')
    descripcion = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(upload_to="obras", null=True, blank=True, verbose_name='Imagen')
    autor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="autor", verbose_name='Autor' )

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''


    def __str__(self):
        return f"{self.id} - {self.titulo}"

class Perfil(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="perfil")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    @property
    def image_url(self):
        return self.avatar.url if self.avatar else ''

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True)
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")
