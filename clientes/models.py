# clientes/models.py

from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el modelo de usuario
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el modelo de usuario
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
