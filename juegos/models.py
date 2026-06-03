from django.db import models

class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.titulo
