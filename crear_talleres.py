#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from cursos.models import Taller, Nivel
from django.utils.text import slugify

# Lista de temas para talleres
temas_talleres = [
    # Redacción y escritura (15 temas)
    "Redacción de textos narrativos", "Redacción de textos descriptivos", "Redacción de textos argumentativos",
    "Redacción de textos expositivos", "Redacción de cuentos cortos", "Redacción de ensayos académicos",
    "Redacción de artículos de opinión", "Redacción de resúmenes y síntesis", "Redacción de informes técnicos",
    "Redacción de cartas formales", "Redacción de correos electrónicos profesionales", "Redacción de currículums vitae",
    "Redacción de discursos", "Redacción de críticas literarias", "Redacción de proyectos de investigación",
    
    # Gramática aplicada (10 temas)
    "Taller de conjugaciones verbales", "Taller de uso del subjuntivo", "Taller de tiempos pasados",
    "Taller de verbos irregulares", "Taller de preposiciones", "Taller de conectores y marcadores",
    "Taller de pronombres personales", "Taller de artículos y determinantes", "Taller de adverbios",
    "Taller de formación de palabras",
    
    # Sintaxis (10 temas)
    "Análisis sintáctico de oraciones simples", "Análisis sintáctico de oraciones compuestas",
    "Identificación de complementos verbales", "Construcción de oraciones subordinadas",
    "Transformación de oraciones activas a pasivas", "Corrección de errores sintácticos",
    "Uso correcto de la concordancia", "Estructura de oraciones condicionales",
    "Estilo directo e indirecto", "Puntuación y estructura sintáctica",
    
    # Ortografía (10 temas)
    "Uso correcto de la B y V", "Uso correcto de la G y J", "Uso correcto de la C, S y Z",
    "Acentuación de palabras", "Uso de la H", "Diptongos e hiatos",
    "Uso de la tilde diacrítica", "Palabras homófonas", "Signos de puntuación",
    "Mayúsculas y reglas ortográficas",
    
    # Comprensión lectora (5 temas)
    "Comprensión de textos literarios", "Comprensión de textos científicos", "Comprensión de textos periodísticos",
    "Lectura crítica y análisis", "Inferencia y deducción en textos",
    
    # Expresión oral (5 temas)
    "Preparación de presentaciones orales", "Técnicas de debate", "Argumentación oral",
    "Exposición de ideas", "Conversación y diálogo",
    
    # Latín (5 temas)
    "Traducción de textos latinos", "Declinaciones latinas", "Verbos latinos",
    "Expresiones latinas en español", "Lectura de textos clásicos",
    
    # Inglés (5 temas)
    "Traducción español-inglés", "Estructuras gramaticales comparadas", "Vocabulario técnico inglés",
    "Redacción de textos bilingües", "Conversación en inglés básico",
]

print("=" * 60)
print("📝 CREANDO 100 TALLERES PARA EL LMS")
print("=" * 60)

talleres_creados = 0

for i in range(1, 101):
    # Seleccionar tema
    tema_idx = (i - 1) % len(temas_talleres)
    tema_base = temas_talleres[tema_idx]
    
    # Determinar nivel según el número
    if i <= 20:
        nivel_texto = "A1 - Principiante"
        nivel_codigo = "a1"
        duracion = 3
    elif i <= 45:
        nivel_texto = "A2 - Básico"
        nivel_codigo = "a2"
        duracion = 5
    elif i <= 70:
        nivel_texto = "B1 - Intermedio"
        nivel_codigo = "b1"
        duracion = 7
    else:
        nivel_texto = "B2 - Intermedio Alto"
        nivel_codigo = "b2"
        duracion = 10
    
    # Crear título único
    titulo = f"Taller {i:03d}: {tema_base} (Nivel {nivel_texto})"
    
    # Crear slug único
    slug_base = slugify(titulo)[:50]
    slug = slug_base
    counter = 1
    while Taller.objects.filter(slug=slug).exists():
        slug = f"{slug_base}-{counter}"
        counter += 1
    
    # Generar instrucciones según el tipo de taller
    if "Redacción" in tema_base or "escritura" in tema_base or "textos" in tema_base:
        instrucciones = f"""
        <h3>📝 Instrucciones del Taller</h3>
        <ol>
            <li>Lee atentamente los materiales proporcionados sobre <strong>{tema_base}</strong>.</li>
            <li>Realiza un borrador de tu texto siguiendo la estructura aprendida.</li>
            <li>Revisa la ortografía y gramática de tu trabajo.</li>
            <li>Comparte tu texto con un compañero para retroalimentación.</li>
            <li>Entrega la versión final en el formato solicitado.</li>
        </ol>
        <h3>📚 Material de apoyo</h3>
        <ul>
            <li>Guía de {tema_base.lower()} (PDF disponible)</li>
            <li>Ejemplos de textos modelo</li>
            <li>Lista de verificación de calidad</li>
        </ul>
        <h3>✅ Criterios de evaluación</h3>
        <ul>
            <li>Estructura y organización del texto (25%)</li>
            <li>Coherencia y cohesión (25%)</li>
            <li>Corrección gramatical y ortográfica (25%)</li>
            <li>Creatividad y originalidad (25%)</li>
        </ul>
        """
    elif "Gramática" in tema_base or "verbos" in tema_base or "conjugaciones" in tema_base:
        instrucciones = f"""
        <h3>📝 Instrucciones del Taller</h3>
        <ol>
            <li>Repasa la teoría sobre <strong>{tema_base}</strong> en los materiales del curso.</li>
            <li>Completa los ejercicios prácticos proporcionados.</li>
            <li>Identifica y corrige errores en oraciones de ejemplo.</li>
            <li>Crea tus propias oraciones aplicando las reglas aprendidas.</li>
            <li>Comparte tus respuestas para revisión.</li>
        </ol>
        <h3>📚 Material de apoyo</h3>
        <ul>
            <li>Tablas de conjugación</li>
            <li>Ejercicios interactivos</li>
            <li>Lista de verbos irregulares</li>
        </ul>
        <h3>✅ Criterios de evaluación</h3>
        <ul>
            <li>Corrección en los ejercicios (40%)</li>
            <li>Aplicación de reglas gramaticales (30%)</li>
            <li>Creatividad en ejemplos propios (30%)</li>
        </ul>
        """
    elif "Lectura" in tema_base or "comprensión" in tema_base:
        instrucciones = f"""
        <h3>📝 Instrucciones del Taller</h3>
        <ol>
            <li>Lee el texto asignado sobre <strong>{tema_base}</strong>.</li>
            <li>Identifica las ideas principales y secundarias.</li>
            <li>Responde las preguntas de comprensión lectora.</li>
            <li>Elabora un resumen del texto leído.</li>
            <li>Prepara una opinión crítica sobre el contenido.</li>
        </ol>
        <h3>📚 Material de apoyo</h3>
        <ul>
            <li>Textos para lectura (nivel adaptado)</li>
            <li>Guía de técnicas de lectura comprensiva</li>
            <li>Vocabulario clave del texto</li>
        </ul>
        <h3>✅ Criterios de evaluación</h3>
        <ul>
            <li>Comprensión del texto (40%)</li>
            <li>Capacidad de síntesis (30%)</li>
            <li>Análisis crítico (30%)</li>
        </ul>
        """
    elif "Oral" in tema_base or "presentación" in tema_base or "debate" in tema_base:
        instrucciones = f"""
        <h3>📝 Instrucciones del Taller</h3>
        <ol>
            <li>Prepara una presentación de 5-7 minutos sobre {tema_base}.</li>
            <li>Utiliza apoyos visuales (diapositivas, pizarra).</li>
            <li>Practica tu dicción y lenguaje corporal.</li>
            <li>Anticipa posibles preguntas del público.</li>
            <li>Presenta frente a un grupo pequeño.</li>
        </ol>
        <h3>📚 Material de apoyo</h3>
        <ul>
            <li>Plantilla de presentación</li>
            <li>Técnicas de oratoria</li>
            <li>Guía de lenguaje no verbal</li>
        </ul>
        <h3>✅ Criterios de evaluación</h3>
        <ul>
            <li>Claridad y estructura de la exposición (30%)</li>
            <li>Dominio del tema (30%)</li>
            <li>Comunicación no verbal (20%)</li>
            <li>Capacidad de respuesta a preguntas (20%)</li>
        </ul>
        """
    else:
        instrucciones = f"""
        <h3>📝 Instrucciones del Taller</h3>
        <ol>
            <li>Revisa el material teórico sobre <strong>{tema_base}</strong>.</li>
            <li>Realiza las actividades prácticas propuestas.</li>
            <li>Documenta tus resultados y aprendizajes.</li>
            <li>Prepara una reflexión final sobre el taller.</li>
            <li>Entrega tu trabajo en la plataforma.</li>
        </ol>
        <h3>📚 Material de apoyo</h3>
        <ul>
            <li>Presentación del tema</li>
            <li>Ejercicios prácticos</li>
            <li>Rúbrica de evaluación</li>
        </ul>
        <h3>✅ Criterios de evaluación</h3>
        <ul>
            <li>Completitud de actividades (40%)</li>
            <li>Calidad del trabajo (30%)</li>
            <li>Reflexión y análisis (30%)</li>
        </ul>
        """
    
    # Crear descripción
    descripcion = f"Taller práctico sobre {tema_base}. Dirigido a estudiantes de nivel {nivel_texto}. Duración estimada: {duracion} días."
    
    # Crear el taller
    taller, created = Taller.objects.get_or_create(
        slug=slug,
        defaults={
            'titulo': titulo,
            'descripcion': descripcion,
            'instrucciones': instrucciones,
            'duracion_dias': duracion
        }
    )
    
    if created:
        talleres_creados += 1
        if talleres_creados <= 20:
            print(f"✅ Taller {talleres_creados:03d}: {titulo[:70]}...")
        elif talleres_creados % 10 == 0:
            print(f"   ... creados {talleres_creados} talleres hasta ahora...")

print("\n" + "=" * 60)
print("📊 BANCO DE TALLERES COMPLETADO")
print("=" * 60)
print(f"✅ Total talleres creados: {talleres_creados}")
print(f"📋 Total talleres en el sistema: {Taller.objects.count()}")

# Estadísticas por nivel (aproximado)
print("\n📊 DISTRIBUCIÓN DE TALLERES:")
print(f"  • Nivel A1 (Principiante): 20 talleres")
print(f"  • Nivel A2 (Básico): 25 talleres")
print(f"  • Nivel B1 (Intermedio): 25 talleres")
print(f"  • Nivel B2 (Intermedio Alto): 30 talleres")

print("\n📂 TALLERES POR CATEGORÍA:")
print(f"  • Redacción y escritura: 15")
print(f"  • Gramática aplicada: 10")
print(f"  • Sintaxis: 10")
print(f"  • Ortografía: 10")
print(f"  • Comprensión lectora: 5")
print(f"  • Expresión oral: 5")
print(f"  • Latín: 5")
print(f"  • Inglés: 5")
