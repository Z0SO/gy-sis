
from django.db import models
from django.contrib.auth.models import User



class Paciente(models.Model):
    pac_dni = models.CharField(max_length=8, unique=True) 
    pac_nombre = models.CharField(max_length=50)
    pac_edad = models.IntegerField()
    pac_domicilio = models.CharField(max_length=100)
    pac_obrasocial = models.CharField(max_length=50)
    pac_telefono = models.CharField(max_length=15)
    pac_telefono_emergencia = models.CharField(max_length=15)
    pac_ocupacion = models.CharField(max_length=50)
    pac_estadocivil = models.CharField(max_length=50)

    # en el admin de django, se muestra el nombre completo
    def __str__(self):
        return self.pac_nombre


# esta historia clinica tiene un unico paciente asociado
class HistoriaClinica(models.Model):
    # related_name='historia_clinica' significa que desde el modelo Paciente, puedo acceder a la historia clinica con el nombre 'historia_clinica'
    # onetoonefield significa que un paciente solo puede tener una historia clinica
    paciente = models.OneToOneField(Paciente, related_name='historia_clinica', on_delete=models.CASCADE)


    motivo_consulta = models.TextField()
    derivado_por = models.CharField(max_length=50)
    antecedentes_clinicos = models.TextField()
    
    # necesita un campo para registrar laboratorio También necesitamos que haya un lugarcito para escribir los laboratorios si es que los solicitamos.
    # Eso puede estar en la historia clínica, luego de antecedentes personales.

    # Los resultados de por ejemplo una extracción de sangre o de orina
    # Por ejemplo: hemoglobina: 13,2
      
    # laboratiorio puede existir o no, es decir, puede ser null
    # hc_laboratorio = models.TextField(blank=True, null=True)
    

    diagnostico_presuntivo = models.TextField()
    tratamientos_anteriores = models.TextField()
    tratamiento_actual = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)




    # en el admin de django, se muestra el nombre del paciente
    def __str__(self):
        return f"Historia Clínica de {self.paciente.pac_nombre}"

# esta revision tiene una unica historia clinica asociada y se puede acceder a ella desde el modelo HistoriaClinica con el nombre 'revisiones'


class ConsultaControl(models.Model):
    # foreignkey significa que una revision tiene una historia clinica asociada
    historia_clinica = models.ForeignKey(HistoriaClinica, related_name='revisiones', on_delete=models.CASCADE)
    fecha_evaluacion = models.DateTimeField(auto_now_add=True)
    
    # lo mismo para laboratorio de consulta control
    cc_laboratorio = models.TextField(blank=True, null=True)
    
    # estado actual es lo que ella llama SINTOMATOLOGIA ACTUAL
    estado_actual = models.TextField()
    indicaciones = models.TextField(blank=True, null=True)

    # en el admin de django, se muestra el nombre del paciente y la fecha
    def __str__(self):
        return f"Revisión de {self.historia_clinica.paciente.pac_nombre} - {self.fecha_evaluacion.strftime('%Y-%m-%d')}"



