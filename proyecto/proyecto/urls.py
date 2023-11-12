
from django.contrib import admin
from django.urls import path, include
from inicio import views as view_m




urlpatterns = [
    
    path('CislamicaA/', admin.site.urls),
    path('', include('auntenticacion.urls')),
    path('miembros/', include('miembros.urls')),
    path('actividades/', include('actividades.urls')),
    path('eventos/', include('eventos.urls')),
    path('gastos/', include('gastos.urls')),
    path('inicios/', include('inicio.urls')),

    path('',view_m.home, name="home"),


# ---------------------ACTIVIDADES EVENTOS-------------------

    

# ---------------------ACTIVIDADES EDUCATIVAS-------------------

    
    # ---------------------NO ACTIVIDADES -------------------

    
 



     
    
  
]

