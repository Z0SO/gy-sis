from django.contrib import admin

from .models import Paciente, HistoriaClinica, ConsultaControl

admin.site.register(Paciente)
admin.site.register(HistoriaClinica)

admin.site.register(ConsultaControl)


