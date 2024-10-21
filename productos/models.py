#clientes app models.py

from django.db import models
from clientes.models import Vendedor  

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)          
    descripcion = models.TextField(blank=True)          

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)       
    nombre = models.CharField(max_length=100)               
    descripcion = models.TextField(blank=True)               
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    cantidad_disponible = models.PositiveIntegerField()      
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)   
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  
    def __str__(self):
        return self.nombre
