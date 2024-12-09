from django.contrib import admin
from .models import Entrada


class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'autor', 'fecha')  # Muestra las columnas en la lista de entradas
    list_filter = ('fecha',)  # Agrega un filtro por fecha
    search_fields = ('titulo', 'subtitulo', 'autor')  # Permite buscar por esos campos
    ordering = ('-fecha',)  # Ordena las entradas por fecha (de más reciente a más antiguo)

# Registrar el modelo con la clase personalizada
admin.site.register(Entrada, EntradaAdmin)
