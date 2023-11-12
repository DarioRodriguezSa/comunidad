from django.contrib import admin
from .models import curso, maestro, status, categoria, clase, tiempo

@admin.register(curso)
class curso(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)

@admin.register(maestro)
class maestro(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',) 

@admin.register(status)
class status(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)   

@admin.register(categoria)
class categoria(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)   

@admin.register(clase)
class clase(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)


@admin.register(tiempo)
class tiempo(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)                  