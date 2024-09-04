"""
las urls de la aplicación historias_clinicas son las siguientes
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, HistoriaClinicaViewSet, RevisionHistoriaViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'historias_clinicas', HistoriaClinicaViewSet)
router.register(r'revisiones', RevisionHistoriaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

por lo que se puede acceder a las siguientes urls
- /url/api/pacientes/
- /url/api/historias_clinicas/
- /url/api/revisiones/
"""
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('historias_clinicas.urls')),
    path('auth/', include('autenticacion.urls')),
]
