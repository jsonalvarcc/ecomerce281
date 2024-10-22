#models.py de la app carritos

from django.db import models
from clientes.models import Cliente  
from productos.models import Producto  

class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)            
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    fecha_creacion = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"Carrito {self.id_carrito} de {self.cliente}"

class CarritoProducto(models.Model):
    id_carrito_producto = models.AutoField(primary_key=True)    
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='productos')  # Relación con Carrito
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  
    cantidad = models.PositiveIntegerField()                  
    def total_precio(self):
        return self.cantidad * self.producto.precio
    def __str__(self):
        return f"{self.cantidad} de {self.producto} en Carrito {self.carrito.id_carrito}"
