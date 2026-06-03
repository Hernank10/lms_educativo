from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.lista_cursos, name='lista'),
    path('<slug:slug>/', views.detalle_curso, name='detalle'),
    path('<slug:curso_slug>/leccion/<int:leccion_id>/', views.leccion_detalle, name='leccion_detalle'),
]
