from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Nivel(models.Model):
    codigo = models.CharField(max_length=2, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    nivel = models.ForeignKey(Nivel, on_delete=models.SET_NULL, null=True, related_name='cursos')
    descripcion = models.TextField()
    duracion_horas = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.titulo} ({self.nivel.codigo if self.nivel else 'Sin nivel'})"

class Leccion(models.Model):
    TIPO_CHOICES = [
        ('teoria', 'Teoría'),
        ('video', 'Video'),
        ('ejercicio', 'Ejercicio'),
        ('quiz', 'Quiz'),
        ('taller', 'Taller'),
    ]
    
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='lecciones')
    titulo = models.CharField(max_length=200)
    orden = models.PositiveIntegerField(default=0)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='teoria')
    contenido_html = models.TextField(blank=True)
    url_video = models.URLField(blank=True)
    duracion_minutos = models.PositiveIntegerField(default=30)
    puntos = models.PositiveIntegerField(default=10)
    
    class Meta:
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.curso.titulo} - {self.titulo}"

class Ejercicio(models.Model):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='ejercicios')
    pregunta = models.TextField()
    respuesta_correcta = models.TextField()
    explicacion = models.TextField(blank=True)
    puntos = models.PositiveIntegerField(default=5)
    orden = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['orden']
    
    def __str__(self):
        return f"Ejercicio: {self.pregunta[:50]}"

class Taller(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    descripcion = models.TextField()
    instrucciones = models.TextField()
    duracion_dias = models.PositiveIntegerField(default=7)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.titulo

class TallerEntrega(models.Model):
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, related_name='entregas')
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    calificacion = models.PositiveIntegerField(default=0)
    comentario_profesor = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['taller', 'estudiante']
    
    def __str__(self):
        return f"{self.taller.titulo} - {self.estudiante.username}"

class Evaluacion(models.Model):
    TIPO_CHOICES = [
        ('diagnostica', 'Diagnóstica'),
        ('formativa', 'Formativa'),
        ('sumativa', 'Sumativa'),
    ]
    
    titulo = models.CharField(max_length=200)
    nivel = models.ForeignKey(Nivel, on_delete=models.SET_NULL, null=True, related_name='evaluaciones')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='formativa')
    descripcion = models.TextField()
    tiempo_limite = models.PositiveIntegerField(default=60)
    puntaje_maximo = models.PositiveIntegerField(default=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"

class Pregunta(models.Model):
    TIPO_CHOICES = [
        ('multiple', 'Opción Múltiple'),
        ('verdadero_falso', 'Verdadero/Falso'),
        ('texto', 'Texto Libre'),
    ]
    
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='preguntas')
    texto = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='multiple')
    puntos = models.PositiveIntegerField(default=5)
    orden = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.evaluacion.titulo} - Pregunta {self.id}"

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto = models.CharField(max_length=500)
    es_correcta = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Opción de {self.pregunta.id}"

class ProgresoUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progreso')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, null=True, blank=True)
    completado = models.BooleanField(default=False)
    puntaje = models.PositiveIntegerField(default=0)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_completado = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ['usuario', 'curso', 'leccion']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.curso.titulo}: {self.puntaje}%"
