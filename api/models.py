from django.db import models

# Create your models here.
class Invitado(models.Model):
    socio = models.CharField(max_length=10)
    fecha_evento = models.DateField()
    ubicacion = models.CharField(max_length=10)
    documento = models.CharField(max_length=11)
    nombre = models.CharField(max_length=20)
    paterno = models.CharField(max_length=20)
    materno = models.CharField(max_length=20)
    observacion = models.CharField(max_length=20,null=True, blank=True)
    pago = models.CharField(max_length=1)
    fecha_autorizacion = models.DateField(null=True, blank=True)
    hora_autorizacion = models.TimeField(null=True, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    hora_ingreso = models.TimeField(null=True, blank=True) 
    
    def __str__(self):
        return self.socio + " - " + str(self.fecha_evento) + " - " + self.ubicacion + " - " + self.paterno  + " - " + self.materno  + " - " + self.nombre
    