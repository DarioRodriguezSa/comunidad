from django.contrib import admin
from .models import tipo, estate

@admin.register(tipo)
class tipo(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)


@admin.register(estate)
class estate(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)    