from django.urls import path
from . import views


app_name = "miembros"
urlpatterns = [
    path('miembros/', views.agregar_miembros, name="agregar_miembro"),
    path('listar_miembros/', views.listar_m, name="lista_miembro"),
    path('delete/<str:miembro_id>/', views.eliminar_miembros, name='eliminar_miembro'),
    path('update/<int:miembro_id>/', views.actualizar_miembro, name='miembros_actuali'),





]
