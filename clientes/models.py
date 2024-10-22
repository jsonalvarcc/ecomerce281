# clientes/models.py

from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    telefono = models.CharField(max_length=15, blank=True)
    coordenadas = models.CharField(max_length=50, blank=True)  # Almacena las coordenadas en formato "latitud,longitud"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    telefono = models.CharField(max_length=15, blank=True)
    coordenadas = models.CharField(max_length=50, blank=True)  # Almacena las coordenadas en formato "latitud,longitud"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
