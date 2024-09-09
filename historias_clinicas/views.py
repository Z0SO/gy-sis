from django.shortcuts import render
from rest_framework import viewsets
from .models import Paciente, HistoriaClinica, ConsultaControl
from .serializers import PacienteSerializer, HistoriaClinicaSerializer, ConsultaControlSerializer

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


class ConsultaControlViewSet(viewsets.ModelViewSet):
    # se obtienen todas las revisiones
    queryset = ConsultaControl.objects.all()

    # se serializan las revisiones
    serializer_class = ConsultaControlSerializer
    permission_classes = [IsAuthenticated]

