from django.db import models
from cursos.models import Curso

class Leccion(models.Model):
    TIPO_CHOICES = [
        ('html', 'Lección HTML'),
        ('python', 'Ejercicio Python'),
        ('juego', 'Juego Interactivo'),
    ]
    
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='lecciones')
    titulo = models.CharField(max_length=200)
    orden = models.PositiveIntegerField(default=0)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='html')
    contenido_html = models.TextField(blank=True)
    url_externa = models.URLField(blank=True)
    
    class Meta:
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.curso.titulo} - {self.titulo}"
