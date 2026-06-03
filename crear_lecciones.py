#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from cursos.models import Curso, Leccion, Nivel
from django.utils.text import slugify

# Obtener los cursos existentes
cursos = list(Curso.objects.all())
if not cursos:
    print("❌ No hay cursos. Crea cursos primero en el admin.")
    exit()

# Temas para las lecciones (40 temas diferentes)
temas = [
    # Gramática (15 temas)
    "El sustantivo y sus tipos", "El adjetivo calificativo", "Los artículos determinados e indeterminados",
    "Los pronombres personales", "Los verbos regulares", "Los verbos irregulares", "Los tiempos del presente",
    "El pretérito perfecto simple", "El pretérito imperfecto", "El futuro simple", "El condicional simple",
    "El subjuntivo presente", "El imperativo afirmativo", "La voz activa y pasiva", "Las perífrasis verbales",
    
    # Sintaxis (10 temas)
    "El sujeto y predicado", "El complemento directo", "El complemento indirecto", "El complemento circunstancial",
    "El complemento agente", "Las oraciones simples", "Las oraciones compuestas", "Las oraciones coordinadas",
    "Las oraciones subordinadas sustantivas", "Las oraciones subordinadas adjetivas",
    
    # Ortografía (10 temas)
    "Uso de la B y V", "Uso de la G y J", "Uso de la C, S y Z", "Uso de la H", "Acentuación de palabras agudas",
    "Acentuación de palabras graves", "Acentuación de palabras esdrújulas", "Los diptongos e hiatos",
    "Los signos de puntuación", "Las mayúsculas y minúsculas",
    
    # Vocabulario (5 temas)
    "Los sinónimos y antónimos", "Los homónimos y parónimos", "Las familias de palabras", "Los campos semánticos",
    "Las expresiones idiomáticas",
]

# Tipos de lección
tipos = ['teoria', 'video', 'ejercicio', 'quiz', 'taller']

# Contenido HTML genérico para lecciones de teoría
def generar_contenido(titulo):
    return f"""
    <div class="leccion-contenido">
        <h2>{titulo}</h2>
        <p>En esta lección aprenderás sobre <strong>{titulo.lower()}</strong>.</p>
        <h3>📖 Explicación teórica</h3>
        <p>El {titulo.lower()} es un concepto fundamental en el aprendizaje del español. 
        A continuación, exploraremos sus características principales y ejemplos prácticos.</p>
        <h3>🎯 Objetivos de la lección</h3>
        <ul>
            <li>Comprender el concepto de {titulo.lower()}</li>
            <li>Identificar ejemplos en diferentes contextos</li>
            <li>Aplicar el conocimiento en ejercicios prácticos</li>
        </ul>
        <h3>📝 Ejemplos</h3>
        <p><strong>Ejemplo 1:</strong> Oración ilustrativa sobre {titulo.lower()}.</p>
        <p><strong>Ejemplo 2:</strong> Oración adicional para reforzar el aprendizaje.</p>
        <p><strong>Ejemplo 3:</strong> Oración con aplicación práctica del tema.</p>
        <h3>💡 Consejos</h3>
        <ul>
            <li>Practica diariamente para reforzar el aprendizaje</li>
            <li>Realiza los ejercicios propuestos</li>
            <li>Consulta la bibliografía recomendada</li>
        </ul>
    </div>
    """

print("=" * 60)
print("📚 CREANDO 100 LECCIONES PARA EL LMS")
print("=" * 60)

lecciones_creadas = 0
curso_espanol = Curso.objects.filter(titulo__icontains='Español').first()
if not curso_espanol:
    curso_espanol = cursos[0]

# Generar 100 lecciones distribuidas en los cursos
for i in range(1, 101):
    # Seleccionar tema (cíclico)
    tema_idx = (i - 1) % len(temas)
    tema_base = temas[tema_idx]
    
    # Variar el título según el número
    if i <= 20:
        nivel_prefix = "A1"
        nivel_texto = "Principiante"
        curso = curso_espanol
    elif i <= 50:
        nivel_prefix = "A2"
        nivel_texto = "Básico"
        curso = curso_espanol
    elif i <= 75:
        nivel_prefix = "B1"
        nivel_texto = "Intermedio"
        curso = curso_espanol
    else:
        nivel_prefix = "B2"
        nivel_texto = "Intermedio Alto"
        curso = curso_espanol
    
    # Crear título único
    titulo = f"Lección {i:03d}: {tema_base} ({nivel_prefix})"
    
    # Seleccionar tipo de lección (cíclico)
    tipo_idx = (i - 1) % len(tipos)
    tipo = tipos[tipo_idx]
    
    # Crear slug único
    slug_base = slugify(titulo)[:50]
    slug = slug_base
    counter = 1
    while Leccion.objects.filter(slug=slug).exists():
        slug = f"{slug_base}-{counter}"
        counter += 1
    
    # Asignar duración y puntos según nivel
    if nivel_prefix == "A1":
        duracion = 20 + (i % 10)
        puntos = 10 + (i % 5)
    elif nivel_prefix == "A2":
        duracion = 25 + (i % 10)
        puntos = 12 + (i % 5)
    else:
        duracion = 30 + (i % 15)
        puntos = 15 + (i % 10)
    
    # Contenido HTML personalizado
    contenido = generar_contenido(titulo)
    
    # Crear la lección
    leccion, created = Leccion.objects.get_or_create(
        curso=curso,
        titulo=titulo,
        defaults={
            'orden': i,
            'tipo': tipo,
            'contenido_html': contenido,
            'duracion_minutos': duracion,
            'puntos': puntos
        }
    )
    
    if created:
        lecciones_creadas += 1
        if lecciones_creadas <= 20:
            print(f"✅ Lección {lecciones_creadas:03d}: {titulo[:60]}... ({tipo}, {duracion} min, {puntos} pts)")
        elif lecciones_creadas % 10 == 0:
            print(f"   ... creadas {lecciones_creadas} lecciones hasta ahora...")

print("\n" + "=" * 60)
print("📊 BANCO DE LECCIONES COMPLETADO")
print("=" * 60)
print(f"✅ Total lecciones creadas: {lecciones_creadas}")
print(f"📖 Total lecciones en el sistema: {Leccion.objects.count()}")

# Estadísticas por tipo
print("\n📊 LECCIONES POR TIPO:")
for tipo in tipos:
    count = Leccion.objects.filter(tipo=tipo).count()
    print(f"  • {tipo}: {count} lecciones")

print("\n📊 LECCIONES POR CURSO:")
for curso in Curso.objects.filter(activo=True):
    count = Leccion.objects.filter(curso=curso).count()
    print(f"  • {curso.titulo[:40]}: {count} lecciones")
