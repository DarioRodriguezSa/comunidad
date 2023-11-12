from django.urls import path
from . import views

app_name = "eventos"
urlpatterns = [

#---------------------EVENTOS------------------------    
    path('eventos_agregar/', views.agregar_evento, name="eventos"),
    path('listar_eventos/', views.list_eventos, name="list_evento"),
    path('deleteeve/<str:evento_id>/', views.eliminar_eventos, name='eliminar_evento'),
    path('updateeve/<int:evento_id>/', views.actualizar_evento, name='evento_actuali'),
    path('genera_pdf/<int:evento_id>/', views.generar_pdf_evento, name='genera_pdf_evento'),




    


]
