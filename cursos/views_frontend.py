from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Curso, Leccion, Ejercicio, Taller, Evaluacion, Pregunta, ProgresoUsuario

def niveles(request):
    """Vista para mostrar niveles A1-C2"""
    from .models import Nivel
    niveles = Nivel.objects.all()
    return render(request, 'cursos/niveles.html', {'niveles': niveles})

def curso_detalle(request, slug):
    curso = get_object_or_404(Curso, slug=slug, activo=True)
    return render(request, 'cursos/curso_detalle.html', {'curso': curso})

@login_required
def leccion_detalle(request, curso_slug, leccion_id):
    curso = get_object_or_404(Curso, slug=curso_slug)
    leccion = get_object_or_404(Leccion, id=leccion_id, curso=curso)
    
    # Registrar progreso
    progreso, created = ProgresoUsuario.objects.get_or_create(
        usuario=request.user,
        curso=curso,
        leccion=leccion
    )
    
    # Obtener ejercicios de la lección
    ejercicios = leccion.ejercicios.all()
    
    return render(request, 'cursos/leccion_detalle.html', {
        'curso': curso,
        'leccion': leccion,
        'ejercicios': ejercicios,
        'progreso': progreso
    })

@login_required
def taller_lista(request):
    talleres = Taller.objects.all()
    return render(request, 'cursos/taller_lista.html', {'talleres': talleres})

@login_required
def evaluacion_realizar(request, evaluacion_id):
    evaluacion = get_object_or_404(Evaluacion, id=evaluacion_id)
    preguntas = evaluacion.preguntas.all()
    return render(request, 'cursos/evaluacion_realizar.html', {
        'evaluacion': evaluacion,
        'preguntas': preguntas
    })
