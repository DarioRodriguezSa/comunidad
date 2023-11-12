from django.urls import path
from . import views

app_name = "actividades"
urlpatterns = [

#---------------------ACTAS MATRIMONIALES------------------------    
    path('actividad/', views.actividads, name="activi"),
    path('actas_agregar/', views.agregar_acta, name="actas"),
    path('listar_nuevos/', views.list_actas, name="list_act"),
    path('deletema/<str:acta_id>/', views.eliminar_actas, name='eliminar_acta'),
    path('updatema/<int:acta_id>/', views.actualizar_acta, name='acta_actuali'),
    path('generar_pdf_acta/<int:acta_id>/', views.generar_pdf_acta, name='generar_pdf_acta'),





# ---------------------ACTIVIDADES EDUCATIVAS-------------------
    path('agregar_actividad/', views.agregar_actividad, name="agregar_act"),
    path('listarm/', views.listar_miem, name="lista"),
    path('listarn/', views.get_tiempo_data, name="datatime"),
    path('lista_edu/', views.lista_educa, name="lista_educativa"),
    path('deleteact/<str:actividad_id>/', views.eliminar_actividades, name='eliminar_actividad'),
    path('updateact/<int:actividad_id>/', views.actualizar_actividad, name='actividad_actuali'),  
    path('generar_pdf_actividad/<int:actividad_id>/', views.generar_pdf_actividad, name='generar_pdf_actividad'),  



    # ---------------------NO ACTIVIDADES -------------------
    path('agregar_noactividad/', views.agregar_noactividad, name="agregar_noact"),
    path('lista_noedu/', views.lista_noeduca, name="lista_noeducativa"),
    path('deletenoact/<str:noactividad_id>/', views.eliminar_noactividades, name='eliminar_noactividad'),
    path('updatenoact/<int:noactividad_id>/', views.actualizar_noactividad, name='noactividad_actuali'), 
    path('generar_pdf_noactividad/<int:noactividad_id>/', views.generar_pdf_noactividad, name='generar_pdf_noactividad'),

    


]
