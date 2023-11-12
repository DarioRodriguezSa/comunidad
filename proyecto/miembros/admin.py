from django.contrib import admin
from .models import nacionalidad, genero, estadocivil, miembro

@admin.register(nacionalidad)
class NacionalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)

@admin.register(genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)


@admin.register(estadocivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)    
