from django.contrib import admin
from .models import Entrada


class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'autor', 'fecha')
    list_filter = ('fecha',) 
    search_fields = ('titulo', 'subtitulo', 'autor')  
    ordering = ('-fecha',) 

admin.site.register(Entrada, EntradaAdmin)
