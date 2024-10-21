from django.contrib import admin
from .models import Carrito, CarritoProducto
from clientes.models import Cliente,Vendedor
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id_carrito', 'cliente', 'fecha_creacion')  # Campos a mostrar
    search_fields = ('cliente__user__username',)  # Busca por nombre de usuario del cliente

@admin.register(CarritoProducto)
class CarritoProductoAdmin(admin.ModelAdmin):
    list_display = ('id_carrito_producto', 'carrito', 'producto', 'cantidad')  # Campos a mostrar
    search_fields = ('carrito__id_carrito', 'producto__nombre')  # Busca por ID del carrito o nombre del producto
