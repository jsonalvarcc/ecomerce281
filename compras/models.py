#models.py de app compras

from django.db import models
from clientes.models import Cliente
from carritos.models import Carrito  # Asegúrate de importar el modelo Carrito

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)  # Campo ID para la compra
    fecha_compra = models.DateTimeField(auto_now_add=True)  # Fecha de la compra
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE)  # Relación con Carrito
    metodo_pago = models.CharField(max_length=50)  # Método de pago (ej: 'Tarjeta de Crédito', 'PayPal', etc.)
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total de la compra

    def __str__(self):
        return f"Compra {self.id_compra} por {self.carrito.cliente} en {self.fecha_compra}"

    