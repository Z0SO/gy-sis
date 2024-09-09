# historias_clinicas/serializers.py

from rest_framework import serializers
from .models import Paciente, HistoriaClinica, ConsultaControl

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'

class ConsultaControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaControl
        fields = '__all__'



