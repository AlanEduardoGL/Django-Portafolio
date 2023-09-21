from django.contrib import admin
from .models import Proyect

# Register your models here.

# Clase para extender las funcinalidades del panel del Admin.
class ProyectAdmin(admin.ModelAdmin):
    # Agregamos los campos de solo lectura al administrador.
    readonly_fields = ('created', 'updated')

# Registramos el modelo "Proyect" y "ProyectAdmin" al administrador Django.
admin.site.register(Proyect, ProyectAdmin)
