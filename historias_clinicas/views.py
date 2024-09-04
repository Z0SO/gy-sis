from django.shortcuts import render
from rest_framework import viewsets
from .models import Paciente, HistoriaClinica, RevisionHistoria
from .serializers import PacienteSerializer, HistoriaClinicaSerializer, RevisionHistoriaSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    # se obtienen todos los pacientes
    queryset = Paciente.objects.all()

    # se serializan los pacientes
    serializer_class = PacienteSerializer


class HistoriaClinicaViewSet(viewsets.ModelViewSet):
    # se obtienen todas las historias clinicas
    queryset = HistoriaClinica.objects.all()

    # se serializan las historias clinicas
    serializer_class = HistoriaClinicaSerializer



class RevisionHistoriaViewSet(viewsets.ModelViewSet):
    # se obtienen todas las revisiones
    queryset = RevisionHistoria.objects.all()

    # se serializan las revisiones
    serializer_class = RevisionHistoriaSerializer


