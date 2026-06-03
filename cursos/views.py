from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso, Leccion, ProgresoUsuario

def lista_cursos(request):
    cursos = Curso.objects.filter(activo=True)
    return render(request, 'cursos/lista.html', {'cursos': cursos})

def detalle_curso(request, slug):
    curso = get_object_or_404(Curso, slug=slug, activo=True)
    return render(request, 'cursos/curso_detalle.html', {'curso': curso})

@login_required
def leccion_detalle(request, curso_slug, leccion_id):
    curso = get_object_or_404(Curso, slug=curso_slug)
    leccion = get_object_or_404(Leccion, id=leccion_id, curso=curso)
    
    progreso, created = ProgresoUsuario.objects.get_or_create(
        usuario=request.user,
        curso=curso,
        leccion=leccion
    )
    
    return render(request, 'cursos/leccion_detalle.html', {
        'curso': curso,
        'leccion': leccion,
        'progreso': progreso
    })
