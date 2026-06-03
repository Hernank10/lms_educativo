from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .models import Curso, Leccion, Nivel, Ejercicio, Taller, Evaluacion, ProgresoUsuario
from django.contrib.auth.models import User

@staff_member_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@staff_member_required
def api_stats(request):
    stats = {
        'cursos': Curso.objects.count(),
        'lecciones': Leccion.objects.count(),
        'usuarios': User.objects.count(),
        'progreso': ProgresoUsuario.objects.count(),
        'niveles': Nivel.objects.count(),
        'ejercicios': Ejercicio.objects.count(),
        'talleres': Taller.objects.count(),
        'evaluaciones': Evaluacion.objects.count(),
    }
    return JsonResponse(stats)

@staff_member_required
def api_list(request, modelo):
    modelos = {
        'usuarios': User.objects.all().values('id', 'username'),
        'cursos': Curso.objects.all().values('id', 'titulo'),
        'niveles': Nivel.objects.all().values('id', 'codigo', 'nombre'),
        'lecciones': Leccion.objects.all().values('id', 'titulo'),
        'ejercicios': Ejercicio.objects.all().values('id', 'pregunta'),
        'talleres': Taller.objects.all().values('id', 'titulo'),
        'evaluaciones': Evaluacion.objects.all().values('id', 'titulo'),
        'progreso': ProgresoUsuario.objects.all().values('id', 'usuario__username', 'curso__titulo', 'puntaje'),
    }
    
    data = list(modelos.get(modelo, []))
    for item in data:
        if 'pregunta' in item:
            item['nombre'] = item['pregunta'][:50]
        elif 'username' in item:
            item['nombre'] = item['username']
        elif 'codigo' in item:
            item['nombre'] = f"{item['codigo']} - {item.get('nombre', '')}"
    
    return JsonResponse(data, safe=False)
