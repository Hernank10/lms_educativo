from django.contrib import admin
from .models import Nivel, Curso, Leccion, Ejercicio, Taller, TallerEntrega, Evaluacion, Pregunta, Opcion, ProgresoUsuario

class LeccionInline(admin.TabularInline):
    model = Leccion
    extra = 1

class EjercicioInline(admin.TabularInline):
    model = Ejercicio
    extra = 1

class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 3

class PreguntaInline(admin.TabularInline):
    model = Pregunta
    extra = 1
    inlines = [OpcionInline]

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'orden']
    list_editable = ['orden']
    search_fields = ['codigo', 'nombre']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'nivel', 'activo', 'duracion_horas']
    list_filter = ['nivel', 'activo']
    search_fields = ['titulo', 'descripcion']
    prepopulated_fields = {'slug': ('titulo',)}
    inlines = [LeccionInline]

@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'curso', 'tipo', 'orden', 'puntos']
    list_filter = ['curso', 'tipo']
    search_fields = ['titulo', 'contenido_html']
    inlines = [EjercicioInline]

@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ['pregunta_corta', 'leccion', 'puntos']
    list_filter = ['leccion__curso']
    search_fields = ['pregunta']
    
    def pregunta_corta(self, obj):
        return obj.pregunta[:50] + "..."
    pregunta_corta.short_description = "Pregunta"

@admin.register(Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'duracion_dias', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion']
    prepopulated_fields = {'slug': ('titulo',)}

@admin.register(TallerEntrega)
class TallerEntregaAdmin(admin.ModelAdmin):
    list_display = ['taller', 'estudiante', 'fecha_entrega', 'calificacion']
    list_filter = ['taller', 'calificacion']
    search_fields = ['estudiante__username']

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'nivel', 'tipo', 'puntaje_maximo']
    list_filter = ['nivel', 'tipo']
    search_fields = ['titulo']
    inlines = [PreguntaInline]

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['texto_corto', 'evaluacion', 'tipo', 'puntos']
    list_filter = ['evaluacion', 'tipo']
    search_fields = ['texto']
    inlines = [OpcionInline]
    
    def texto_corto(self, obj):
        return obj.texto[:50] + "..."
    texto_corto.short_description = "Pregunta"

@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'texto_corto', 'es_correcta']
    list_filter = ['es_correcta']
    search_fields = ['texto']
    
    def texto_corto(self, obj):
        return obj.texto[:50] + "..."
    texto_corto.short_description = "Opción"

@admin.register(ProgresoUsuario)
class ProgresoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'curso', 'leccion', 'completado', 'puntaje']
    list_filter = ['curso', 'completado']
    search_fields = ['usuario__username']
