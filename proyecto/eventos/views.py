from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Q
from eventos.models import evento, estate, tipo
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle
from django.utils import timezone
from .models import evento





#-----------------------------APARTADO DE MODULO DE EVENTOS---------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

@login_required(login_url="auth/login/")
def generar_pdf_evento(request, evento_id):
    try:
        evento_seleccionado = evento.objects.get(pk=evento_id)
    except evento.DoesNotExist:
        return HttpResponse('El evento no existe')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="evento_{evento_seleccionado.id}.pdf'

    doc = SimpleDocTemplate(response, pagesize=landscape(letter))

    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_body = styles['Normal']

    elements = []

    fecha_actual = timezone.now().strftime("%Y-%m-%d")


    elements.append(Paragraph('<u>COMUNIDAD ISLÁMICA ALDAAWA</u>', style_title))
    elements.append(Paragraph('<u>Eventos</u>', style_title))
    elements.append(Spacer(1, 12))

    content = [
        [Paragraph('<b>Título:</b>', style_body), evento_seleccionado.titulo],
        [Paragraph('<b>Tipo:</b>', style_body), evento_seleccionado.tipo.nombre],
        [Paragraph('<b>Estado:</b>', style_body), evento_seleccionado.estate.nombre],
        [Paragraph('<b>Invitante:</b>', style_body), evento_seleccionado.invitante],
        [Paragraph('<b>Fecha:</b>', style_body), str(evento_seleccionado.fecha)],
        [Paragraph('<b>Encargado:</b>', style_body), evento_seleccionado.encargado],
        [Paragraph('<b>Lugar:</b>', style_body), evento_seleccionado.lugar],
        [Paragraph('<b>Número de Asistentes:</b>', style_body), str(evento_seleccionado.noasistentes)],
        [Paragraph('<b>Staff:</b>', style_body), evento_seleccionado.staff],
    ]
    elements.append(Paragraph(f'<u>Fecha de Impresión: {fecha_actual}</u>'))
    elements.append(Paragraph('<u>_</u>'))

    table = Table(content)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return response


#Lista los Eventos ya creados en la base de datos
@login_required(login_url="auth/login/")
def list_eventos(request):
    query = request.GET.get('q', '')
    eventos = evento.objects.filter(
        Q(titulo__icontains=query) |  
        Q(invitante__icontains=query) |      
        Q(fecha__icontains=query) | 
        Q(encargado__icontains=query) | 
        Q(staff__icontains=query) |
        Q(lugar__icontains=query) | 
        Q(noasistentes__icontains=query) |      
        Q(estate__nombre__icontains=query) |   
        Q(tipo__nombre__icontains=query)        
    )
    context = {
        "active_icon": "eventos",
        "eventos":eventos,
        "query": query,
    }
    return render(request, "evento/eventos.html", context)









#Agrega a la base de datos los Eventos, funcion para insertar 
@login_required(login_url="auth/login/")
def agregar_evento(request):
    tipos = tipo.objects.all()
    estates = estate.objects.all()

    if request.method == 'POST':
        data = request.POST
        titulo = data['titulo']

        # Verifica si ya existe un evento con el mismo título
        if evento.objects.filter(titulo=titulo).exists():
            messages.error(request, 'Ya existe un evento registrado con ese Título.', extra_tags="danger")
            return redirect('eventos:eventos')

        try:
            tipo_obj = tipo.objects.get(pk=data['tipo'])
            estate_obj = estate.objects.get(pk=data['estate'])

            nuevo_evento = evento(
                tipo=tipo_obj,
                estate=estate_obj,
                titulo=titulo,
                invitante=data['invitante'],
                fecha=data['fecha'],
                encargado=data['encargado'],
                lugar=data['lugar'],
                noasistentes=data['noasistentes'],
                staff=data['staff']
            )
            nuevo_evento.save()

            messages.success(request, 'Evento Creado con éxito!', extra_tags="success")
            return redirect('eventos:eventos')

        except Exception as e:
            messages.error(request, 'Error al crear el Evento: ' + str(e), extra_tags="danger")
            return redirect('eventos:evento')

    return render(request, "evento/agregar_evento.html", {
        'tipos': tipos,
        'estates': estates,
    })



#Funcion que elimina un evento de la mezquita
@login_required(login_url="auth/login/")
def eliminar_eventos(request, evento_id):
    try:
        ACtivi = evento.objects.get(pk=evento_id)
        ACtivi.delete()
        messages.success(request, '¡Evento eliminado!', extra_tags="success")
        return redirect('eventos:list_evento')  
    except Exception as e:
        messages.error(request, '¡Hubo un error durante la eliminación!' + str(e), extra_tags="danger")
        return redirect('evento:list_evento')
    



#actualiza los eventos de la mezquita
@login_required(login_url="auth/login/")
def actualizar_evento(request, evento_id):
    tipos = tipo.objects.all()
    estates = estate.objects.all()

    try:
        evento_obj = evento.objects.get(pk=evento_id)

        if request.method == 'POST':
            data = request.POST
            nuevo_titulo = data['titulo']

            # Verifica si ya existe otro evento con el mismo título (excepto el actual)
            if nuevo_titulo != evento_obj.titulo and evento.objects.filter(titulo=nuevo_titulo).exists():
                messages.error(request, 'Ya existe un evento registrado con ese Título.', extra_tags="danger")
                return redirect('eventos:eventos')

            tipo_obj = tipo.objects.get(pk=data['tipo'])
            estate_obj = estate.objects.get(pk=data['estate'])

            # Actualiza los campos del evento excepto el título
            evento_obj.tipo = tipo_obj
            evento_obj.estate = estate_obj
            evento_obj.invitante = data['invitante']
            evento_obj.fecha = data['fecha']
            evento_obj.encargado = data['encargado']
            evento_obj.lugar = data['lugar']
            evento_obj.noasistentes = data['noasistentes']
            evento_obj.staff = data['staff']
            evento_obj.titulo = nuevo_titulo  # Actualiza el título

            evento_obj.save()

            messages.success(request, 'Evento actualizado con éxito!', extra_tags="success")
            return redirect('eventos:list_evento')

        return render(request, "evento/actualizar_evento.html", {
            'evento': evento_obj,
            'tipos': tipos,
            'estates': estates,
        })

    except evento.DoesNotExist:
        messages.error(request, 'El evento que intentas actualizar no existe.', extra_tags="danger")
        return redirect('eventos:list_evento')
    except Exception as e:
        messages.error(request, 'Error al actualizar el evento: ' + str(e), extra_tags="danger")
        return redirect('eventos:list_evento')