from django.contrib import admin
from .models import Cliente, Vendedor

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'user_first_name', 'user_last_name', 'user_email')
    
    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'Nombre'

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = 'Apellido'
    
    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Correo Electrónico'

admin.site.register(Cliente, ClienteAdmin)

class VendedorAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'user_first_name', 'user_last_name', 'user_email')
    
    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'Nombre'

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = 'Apellido'

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Correo Electrónico'



# Registro de modelos en el admin
admin.site.register(Vendedor, VendedorAdmin)
