from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso, Leccion, Ejercicio, Taller, Evaluacion, ProgresoUsuario

@login_required
def student_dashboard(request):
    context = {
        'cursos': Curso.objects.filter(activo=True),
        'lecciones': Leccion.objects.all().select_related('curso'),
        'ejercicios': Ejercicio.objects.all(),
        'talleres': Taller.objects.all(),
        'evaluaciones': Evaluacion.objects.all(),
        'total_lecciones': Leccion.objects.count(),
        'total_ejercicios': Ejercicio.objects.count(),
        'total_talleres': Taller.objects.count(),
        'total_evaluaciones': Evaluacion.objects.count(),
    }
    return render(request, 'student_dashboard.html', context)

@login_required
def continuar_curso(request, slug):
    curso = get_object_or_404(Curso, slug=slug)
    lecciones_completadas = ProgresoUsuario.objects.filter(
        usuario=request.user, 
        curso=curso, 
        completado=True
    )
    siguiente_leccion = curso.lecciones.exclude(
        id__in=lecciones_completadas.values('leccion_id')
    ).first()
    
    if siguiente_leccion:
        return render(request, 'cursos/leccion_detalle.html', {
            'curso': curso, 
            'leccion': siguiente_leccion
        })
    return render(request, 'cursos/curso_completado.html', {'curso': curso})
