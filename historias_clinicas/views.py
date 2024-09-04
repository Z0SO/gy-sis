from django.shortcuts import render
from rest_framework import viewsets
from .models import Paciente, HistoriaClinica, RevisionHistoria
from .serializers import PacienteSerializer, HistoriaClinicaSerializer, RevisionHistoriaSerializer

from rest_framework.permissions import IsAuthenticated

class PacienteViewSet(viewsets.ModelViewSet):
    # se obtienen todos los pacientes
    queryset = Paciente.objects.all()

    # se serializan los pacientes
    serializer_class = PacienteSerializer
    permission_classes = [IsAuthenticated]

class HistoriaClinicaViewSet(viewsets.ModelViewSet):
    # se obtienen todas las historias clinicas
    queryset = HistoriaClinica.objects.all()

    # se serializan las historias clinicas
    serializer_class = HistoriaClinicaSerializer

    # con drf jwt se obtiene el usuario autenticado
    permission_classes = [IsAuthenticated]


class RevisionHistoriaViewSet(viewsets.ModelViewSet):
    # se obtienen todas las revisiones
    queryset = RevisionHistoria.objects.all()

    # se serializan las revisiones
    serializer_class = RevisionHistoriaSerializer
    permission_classes = [IsAuthenticated]

