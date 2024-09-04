# historias_clinicas/urls.py

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
