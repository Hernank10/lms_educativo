#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from cursos.models import Evaluacion, Pregunta, Opcion, Nivel, Curso

# Obtener niveles
a1 = Nivel.objects.get(codigo='A1')
a2 = Nivel.objects.get(codigo='A2')
b1 = Nivel.objects.get(codigo='B1')

print("=" * 50)
print("📝 CREANDO BANCO DE EVALUACIONES")
print("=" * 50)

# ========== EVALUACIÓN A1: ESPAÑOL PRINCIPIANTES ==========
eval_a1, created = Evaluacion.objects.get_or_create(
    titulo="Evaluacion Nivel A1 - Español Principiantes",
    defaults={
        'nivel': a1,
        'tipo': 'formativa',
        'descripcion': 'Evalua tus conocimientos basicos de español. Incluye vocabulario, gramatica y comprension.',
        'tiempo_limite': 60,
        'puntaje_maximo': 100
    }
)
print(f"{'✅ CREADA' if created else '⚠️ YA EXISTE'}: {eval_a1.titulo}")

# Preguntas para evaluación A1
preguntas_a1 = [
    {"texto": "¿Como se dice 'Hello' en español?", "tipo": "multiple", "puntos": 5, "opciones": [("Adios", False), ("Buenas noches", False), ("Hola", True), ("Gracias", False)]},
    {"texto": "¿Cual es el numero 15 en español?", "tipo": "multiple", "puntos": 5, "opciones": [("Cincuenta", False), ("Quince", True), ("Cinco", False), ("Catorce", False)]},
    {"texto": "Completa: 'Yo ______ (ser) estudiante'", "tipo": "multiple", "puntos": 5, "opciones": [("eres", False), ("es", False), ("soy", True), ("somos", False)]},
    {"texto": "¿Cual es el femenino de 'profesor'?", "tipo": "multiple", "puntos": 5, "opciones": [("profesora", True), ("profesor", False), ("profesoro", False), ("profesorina", False)]},
    {"texto": "Selecciona el saludo correcto para la manana:", "tipo": "multiple", "puntos": 5, "opciones": [("Buenas tardes", False), ("Buenos dias", True), ("Buenas noches", False), ("Hola", False)]},
    {"texto": "¿Que significa 'gracias' en ingles?", "tipo": "multiple", "puntos": 5, "opciones": [("Please", False), ("Sorry", False), ("Thank you", True), ("Hello", False)]},
    {"texto": "Completa: 'Ellos ______ (vivir) en Madrid'", "tipo": "multiple", "puntos": 5, "opciones": [("vivo", False), ("vives", False), ("vive", False), ("viven", True)]},
    {"texto": "¿Cual es el opuesto de 'grande'?", "tipo": "multiple", "puntos": 5, "opciones": [("alto", False), ("pequeno", True), ("gordo", False), ("largo", False)]},
    {"texto": "Selecciona el dia de la semana:", "tipo": "multiple", "puntos": 5, "opciones": [("Enero", False), ("Verano", False), ("Lunes", True), ("Ayer", False)]},
    {"texto": "¿Como se dice 'La casa es bonita' en ingles?", "tipo": "multiple", "puntos": 5, "opciones": [("The house is big", False), ("The house is beautiful", True), ("The car is nice", False), ("The home is good", False)]},
    {"texto": "Completa: 'Maria ______ (tener) 20 anos'", "tipo": "multiple", "puntos": 5, "opciones": [("tengo", False), ("tienes", False), ("tiene", True), ("tenemos", False)]},
    {"texto": "¿Cual es el color 'azul' en ingles?", "tipo": "multiple", "puntos": 5, "opciones": [("Red", False), ("Green", False), ("Blue", True), ("Yellow", False)]},
    {"texto": "Selecciona la fruta:", "tipo": "multiple", "puntos": 5, "opciones": [("zanahoria", False), ("manzana", True), ("lechuga", False), ("tomate", False)]},
    {"texto": "¿Que verbo usarias para hablar de hambre?", "tipo": "multiple", "puntos": 5, "opciones": [("tener", True), ("ser", False), ("estar", False), ("haber", False)]},
    {"texto": "Completa: 'Ayer ______ (ir) al cine'", "tipo": "multiple", "puntos": 5, "opciones": [("voy", False), ("fui", True), ("iba", False), ("ire", False)]},
    {"texto": "¿Cual es el plural de 'mes'?", "tipo": "multiple", "puntos": 5, "opciones": [("meses", True), ("mes", False), ("mesos", False), ("mesas", False)]},
    {"texto": "Selecciona el animal:", "tipo": "multiple", "puntos": 5, "opciones": [("mesa", False), ("perro", True), ("casa", False), ("libro", False)]},
    {"texto": "¿Que significa 'rapidamente'?", "tipo": "multiple", "puntos": 5, "opciones": [("Slowly", False), ("Quickly", True), ("Carefully", False), ("Loudly", False)]},
    {"texto": "Completa: 'Nosotros ______ (estudiar) mucho'", "tipo": "multiple", "puntos": 5, "opciones": [("estudia", False), ("estudian", False), ("estudiamos", True), ("estudio", False)]},
    {"texto": "¿Cual es la despedida mas comun?", "tipo": "multiple", "puntos": 5, "opciones": [("Hola", False), ("Adios", True), ("Gracias", False), ("Por favor", False)]},
]

for i, p in enumerate(preguntas_a1, 1):
    pregunta, created = Pregunta.objects.get_or_create(
        evaluacion=eval_a1,
        texto=p["texto"],
        defaults={'tipo': p["tipo"], 'puntos': p["puntos"], 'orden': i}
    )
    if created:
        for opcion_texto, es_correcta in p["opciones"]:
            Opcion.objects.create(pregunta=pregunta, texto=opcion_texto, es_correcta=es_correcta)
        print(f"  ✅ Pregunta {i} creada")
    else:
        print(f"  ⚠️ Pregunta {i} ya existe")

print(f"\n📊 Evaluacion A1: {Pregunta.objects.filter(evaluacion=eval_a1).count()} preguntas")

# ========== EVALUACIÓN A2: ESPAÑOL BÁSICO ==========
eval_a2, created = Evaluacion.objects.get_or_create(
    titulo="Evaluacion Nivel A2 - Español Basico",
    defaults={
        'nivel': a2,
        'tipo': 'formativa',
        'descripcion': 'Demuestra tus conocimientos en español intermedio bajo.',
        'tiempo_limite': 70,
        'puntaje_maximo': 100
    }
)
print(f"\n{'✅ CREADA' if created else '⚠️ YA EXISTE'}: {eval_a2.titulo}")

preguntas_a2 = [
    {"texto": "¿Cual es el preterito perfecto de 'cantar'?", "tipo": "multiple", "puntos": 5, "opciones": [("cantaba", False), ("cante", True), ("canto", False), ("cantaria", False)]},
    {"texto": "Completa: 'Si tuviera dinero, ______ (viajar) a Paris'", "tipo": "multiple", "puntos": 5, "opciones": [("viajaria", True), ("viajo", False), ("viaje", False), ("viajare", False)]},
    {"texto": "¿Que significa 'despertarse'?", "tipo": "multiple", "puntos": 5, "opciones": [("Dormir", False), ("Levantarse despues de dormir", True), ("Comer", False), ("Trabajar", False)]},
    {"texto": "Selecciona el antonimo de 'alegre'", "tipo": "multiple", "puntos": 5, "opciones": [("feliz", False), ("contento", False), ("triste", True), ("animado", False)]},
    {"texto": "Completa: 'Antes de ______ (salir), apaga la luz'", "tipo": "multiple", "puntos": 5, "opciones": [("salir", True), ("sales", False), ("saliendo", False), ("saliste", False)]},
]

for i, p in enumerate(preguntas_a2, 1):
    pregunta, created = Pregunta.objects.get_or_create(
        evaluacion=eval_a2,
        texto=p["texto"],
        defaults={'tipo': p["tipo"], 'puntos': p["puntos"], 'orden': i}
    )
    if created:
        for opcion_texto, es_correcta in p["opciones"]:
            Opcion.objects.create(pregunta=pregunta, texto=opcion_texto, es_correcta=es_correcta)
        print(f"  ✅ Pregunta {i} creada")

print(f"\n📊 Evaluacion A2: {Pregunta.objects.filter(evaluacion=eval_a2).count()} preguntas")

# ========== EVALUACIÓN DE LATÍN ==========
eval_latin, created = Evaluacion.objects.get_or_create(
    titulo="Evaluacion de Latin - Declinaciones",
    defaults={
        'nivel': None,
        'tipo': 'formativa',
        'descripcion': 'Pon a prueba tus conocimientos sobre las declinaciones latinas.',
        'tiempo_limite': 45,
        'puntaje_maximo': 100
    }
)
print(f"\n{'✅ CREADA' if created else '⚠️ YA EXISTE'}: {eval_latin.titulo}")

preguntas_latin = [
    {"texto": "¿Cual es el genitivo singular de 'rosa' (1ª declinacion)?", "tipo": "multiple", "puntos": 10, "opciones": [("rosae", True), ("rosam", False), ("rosa", False), ("rosarum", False)]},
    {"texto": "¿Que caso expresa el complemento agente en latin?", "tipo": "multiple", "puntos": 10, "opciones": [("Nominativo", False), ("Acusativo", False), ("Ablativo", True), ("Genitivo", False)]},
    {"texto": "Traduce 'servus' (2ª declinacion)", "tipo": "multiple", "puntos": 10, "opciones": [("Senor", False), ("Esclavo", True), ("Amigo", False), ("Enemigo", False)]},
]

for i, p in enumerate(preguntas_latin, 1):
    pregunta, created = Pregunta.objects.get_or_create(
        evaluacion=eval_latin,
        texto=p["texto"],
        defaults={'tipo': p["tipo"], 'puntos': p["puntos"], 'orden': i}
    )
    if created:
        for opcion_texto, es_correcta in p["opciones"]:
            Opcion.objects.create(pregunta=pregunta, texto=opcion_texto, es_correcta=es_correcta)
        print(f"  ✅ Pregunta {i} creada")

print(f"\n📊 Evaluacion Latin: {Pregunta.objects.filter(evaluacion=eval_latin).count()} preguntas")

# Estadisticas finales
print("\n" + "="*50)
print("📊 BANCO DE EVALUACIONES CREADO")
print("="*50)
print(f"Total evaluaciones: {Evaluacion.objects.count()}")
for e in Evaluacion.objects.all():
    print(f"  • {e.titulo} ({e.preguntas.count()} preguntas)")
print(f"\nTotal preguntas: {Pregunta.objects.count()}")
print(f"Total opciones: {Opcion.objects.count()}")
