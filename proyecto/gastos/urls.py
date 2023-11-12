from django.urls import path
from . import views

app_name = "gastos"
urlpatterns = [

#---------------------EVENTOS------------------------    
    path('gastos_agregar/', views.agregar_gasto, name="gastos"),
    path('listar_gastos/', views.list_gastos, name="list_gasto"),
    path('deletegas/<str:gasto_id>/', views.eliminar_gastos, name='eliminar_gasto'),
    path('updategas/<int:gasto_id>/', views.actualizar_gasto, name='gastos_actuali'),
    path('_gasgenera_pdf/<int:gasto_id>/', views.generar_pdf_gasto, name='gastos_pdf'),






    


]
