from statistics import mode
from django.db import models

# Create your models here.
class Host(models.Model):
    ip = models.CharField(max_length=15, default='No ip', help_text='Direccion IP')
    app = models.CharField(max_length=15, default='No ip', help_text='Aplicacion')
    is_server = models.BooleanField(default=False, help_text='Equipo es un servidor?')
    has_ping =  models.BooleanField(default=False, help_text='Hay conexion?')
    is_from_sim =  models.BooleanField(default=False, help_text='Es de la sala de simulacion?')
