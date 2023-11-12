from datetime import date
from django.shortcuts import render
from actividades.models import actividad, noactividad
from eventos.models import evento
from django.contrib.auth.decorators import login_required

@login_required(login_url="auth/login/")
def home(request):
    # Obten la fecha actual
    today = date.today()
    
    # Filtra las actividades basadas en la fecha y estado
    actividades = actividad.objects.filter(fechafin__lte=today, status__nombre='En Proceso')
    noactividades = noactividad.objects.filter(fechafin__lte=today, status__nombre='En Proceso')
    eventos = evento.objects.filter(estate__nombre='En Proceso')
    
    actividades_message = None
    noactividades_message = None
    eventos_message = None

    if actividades:
        actividades_message = "Hay actividades de Miembros en proceso que requieren actualización. Por favor, verifica y actualiza su Estado."

    if noactividades:
        noactividades_message = "Hay actividades de No Miembros en proceso que requieren actualización. Por favor, verifica y actualiza su Estado."
        
    if eventos:
        eventos_message = "Hay eventos en proceso, Actualiza su estado cuando finalicen."

    context = {
        "active_icon": "actividades",
        "actividades": actividades,
        "noactividades": noactividades,
        "eventos": eventos,
        "actividades_message": actividades_message,
        "noactividades_message": noactividades_message,
        "eventos_message": eventos_message,
    }
    return render(request, "inicio/home.html", context)
