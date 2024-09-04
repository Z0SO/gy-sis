from django.contrib import admin

from .models import Paciente, HistoriaClinica, RevisionHistoria

admin.site.register(Paciente)
admin.site.register(HistoriaClinica)


admin.site.register(RevisionHistoria)

