from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre', 'descripcion')  # Campos a mostrar en la lista
    search_fields = ('nombre',)  # Campo de búsqueda

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'precio', 'cantidad_disponible', 'vendedor', 'categoria')  # Campos a mostrar en la lista
    search_fields = ('nombre',)  # Campo de búsqueda
    list_filter = ('categoria', 'vendedor')  # Filtros para la lista

