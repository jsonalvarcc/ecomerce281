from django.contrib import admin
from .models import Cliente, Vendedor

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'email')
    search_fields = ('user__username', 'user__email', 'telefono')
    list_filter = ('telefono',)
    
    # Detalles al ver un cliente
    fieldsets = (
        (None, {
            'fields': ('user', 'telefono')
        }),
        ('Información Adicional', {
            'fields': ('user__first_name', 'user__last_name', 'user__email'),
            'classes': ('collapse',),
        }),
    )

    def email(self, obj):
        return obj.user.email
    email.short_description = 'Correo Electrónico'

class VendedorAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'email')
    search_fields = ('user__username', 'user__email', 'telefono')
    list_filter = ('telefono',)

    # Detalles al ver un vendedor
    fieldsets = (
        (None, {
            'fields': ('user', 'telefono')
        }),
        ('Información Adicional', {
            'fields': ('user__first_name', 'user__last_name', 'user__email'),
            'classes': ('collapse',),
        }),
    )

    def email(self, obj):
        return obj.user.email
    email.short_description = 'Correo Electrónico'

# Registro de modelos en el admin
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Vendedor, VendedorAdmin)
