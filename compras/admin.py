from django.contrib import admin
from .models import Compra

class CompraAdmin(admin.ModelAdmin):
    list_display = ('id_compra', 'carrito', 'fecha_compra', 'metodo_pago', 'total')
    search_fields = ('carrito__cliente__user__username', 'metodo_pago')  # Puedes buscar por nombre de usuario del cliente

admin.site.register(Compra, CompraAdmin)
