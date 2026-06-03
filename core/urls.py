from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from cursos.admin_views import admin_dashboard, api_stats, api_list
from cursos.student_views import student_dashboard, continuar_curso

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('admin-panel/', admin_dashboard, name='admin_panel'),
    path('mi-panel/', student_dashboard, name='student_dashboard'),
    path('continuar/<slug:slug>/', continuar_curso, name='continuar_curso'),
    path('cursos/', include('cursos.urls')),
    path('api/stats/', api_stats, name='api_stats'),
    path('admin-api/<str:modelo>/', api_list, name='api_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
