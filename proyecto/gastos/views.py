from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Q
from eventos.models import evento
from gastos.models import gasto
from django.contrib.auth.decorators import login_required
from decimal import Decimal  
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle
from django.utils import timezone






#-----------------------------APARTADO DE MODULO DE EVENTOS---------------------------------------------
#----------------------------------------------------------------------------------------------------------------------


@login_required(login_url="auth/login/")
def generar_pdf_gasto(request, gasto_id):
    try:
        gasto_seleccionado = gasto.objects.get(pk=gasto_id)
    except gasto.DoesNotExist:
        return HttpResponse('El gasto no existe')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="gasto_{gasto_seleccionado.id}.pdf'

    doc = SimpleDocTemplate(response, pagesize=landscape(letter))

    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_body = styles['Normal']

    elements = []

    fecha_actual = timezone.now().strftime("%Y-%m-%d")


    elements.append(Paragraph('<u>COMUNIDAD ISLÁMICA ALDAAWA</u>', style_title))
    elements.append(Paragraph('<u>Gastos</u>', style_title))
    elements.append(Spacer(1, 12))

    content = [
        [Paragraph('<b>Evento:</b>', style_body), gasto_seleccionado.eventoa.titulo],
        [Paragraph('<b>Presupuesto:</b>', style_body), f'Q. {gasto_seleccionado.presupuesto} °°'],
        [Paragraph('<b>Transporte:</b>', style_body), f'Q. {gasto_seleccionado.transporte} °°'],
        [Paragraph('<b>Personal:</b>', style_body), f'Q. {gasto_seleccionado.personal} °°'],
        [Paragraph('<b>Combustible:</b>', style_body), f'Q. {gasto_seleccionado.combustible} °°'],
        [Paragraph('<b>Alquiler:</b>', style_body), f'Q. {gasto_seleccionado.alquiler} °°'],
        [Paragraph('<b>Viáticos:</b>', style_body), f'Q. {gasto_seleccionado.viaticos} °°'],
        [Paragraph('<b>Donaciones:</b>', style_body), f'Q. {gasto_seleccionado.donaciones} °°'],
        [Paragraph('<b>Otros:</b>', style_body), f'Q. {gasto_seleccionado.otros} °°'],
        [Paragraph('<b>Total Gastado:</b>', style_body), f'Q. {gasto_seleccionado.residuo} °°'],
        [Paragraph('<b>Sobrante:</b>', style_body), f'Q. {gasto_seleccionado.totalgastado} °°'],
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
def list_gastos(request):
    query = request.GET.get('q', '')
    gastos = gasto.objects.filter(  
        Q(eventoa__titulo__icontains=query)        
    )
    context = {
        "active_icon": "gastos",
        "gastos":gastos,
        "query": query,
    }
    return render(request, "gasto/gastos.html", context)






@login_required(login_url="auth/login/")
def eliminar_gastos(request, gasto_id):
    try:
        Gasto = gasto.objects.get(pk=gasto_id)
        Gasto.delete()
        messages.success(request, '¡Gasto eliminado!', extra_tags="success")
        return redirect('gastos:list_gasto')  
    except Exception as e:
        messages.error(request, '¡Hubo un error durante la eliminación!' + str(e), extra_tags="danger")
        return redirect('gastos:list_gasto')
    





#Agrega a la base de datos los Eventos, funcion para insertar 
@login_required(login_url="auth/login/")
def agregar_gasto(request):
    eventos = evento.objects.all()

    if request.method == 'POST':
        data = request.POST

        evento_id = data.get('evento')

        # Verificar si ya existe un gasto asociado al evento
        if gasto.objects.filter(eventoa__id=evento_id).exists():
            messages.error(request, 'Ya existe un gasto registrado para este evento.', extra_tags="danger")
            return redirect('gastos:list_gasto')

        # Elimina "Q." de los valores ingresados
        presupuesto = re.sub(r'[^\d.]', '', data.get('presupuesto'))
        transporte = re.sub(r'[^\d.]', '', data.get('transporte'))
        personal = re.sub(r'[^\d.]', '', data.get('personal'))
        combustible = re.sub(r'[^\d.]', '', data.get('combustible'))
        alquiler = re.sub(r'[^\d.]', '', data.get('alquiler'))
        viaticos = re.sub(r'[^\d.]', '', data.get('viaticos'))
        donaciones = re.sub(r'[^\d.]', '', data.get('donaciones'))
        otros = re.sub(r'[^\d.]', '', data.get('otros'))

        # Validación de los valores ingresados
        if not presupuesto or \
           not transporte or \
           not personal or \
           not combustible or \
           not alquiler or \
           not viaticos or \
           not donaciones or \
           not otros:
            messages.error(request, 'Los valores ingresados deben ser numéricos.', extra_tags="danger")
            return redirect('gastos:gastos')

        # Convertir los valores a números de punto flotante
        presupuesto = float(presupuesto)
        transporte = float(transporte)
        personal = float(personal)
        combustible = float(combustible)
        alquiler = float(alquiler)
        viaticos = float(viaticos)
        donaciones = float(donaciones)
        otros = float(otros)

        evento_obj = evento.objects.get(pk=evento_id)

        # Calcula el totalgastado y residuo
        totalgastado = presupuesto - (transporte + personal + combustible + alquiler + viaticos + donaciones + otros)
        residuo = presupuesto - totalgastado

        nuevo_evento = gasto(
            eventoa=evento_obj,
            presupuesto=presupuesto,
            transporte=transporte,
            personal=personal,
            combustible=combustible,
            alquiler=alquiler,
            viaticos=viaticos,
            donaciones=donaciones,
            otros=otros,
            totalgastado=totalgastado,
            residuo=residuo
        )
        nuevo_evento.save()

        messages.success(request, 'Gasto creado con éxito!', extra_tags="success")
        return redirect('gastos:gastos')

    return render(request, "gasto/agregar_gasto.html", {
        'eventos': eventos,
    })











#Actualiza un gasto de un evento realizado en la mezquita aldaawa
@login_required(login_url="auth/login/")
def actualizar_gasto(request, gasto_id):
    eventos = evento.objects.all()

    try:
        gasto_obj = gasto.objects.get(pk=gasto_id)

        if request.method == 'POST':
            data = request.POST.copy()  # Crea una copia mutable de request.POST

            evento_id = data.get('evento')

            if gasto_obj.eventoa.id != int(evento_id):
                # Verifica si ya existe un gasto asociado al nuevo evento
                if gasto.objects.filter(eventoa__id=evento_id).exclude(id=gasto_obj.id).exists():
                    messages.error(request, 'Ya existe un gasto registrado para este evento.', extra_tags="danger")
                    return redirect('gastos:list_gasto')

                evento_obj = evento.objects.get(pk=evento_id)
                gasto_obj.eventoa = evento_obj

            # Reemplaza comas con puntos en los valores
            for key in ['presupuesto', 'transporte', 'personal', 'combustible', 'alquiler', 'viaticos', 'donaciones', 'otros']:
                data[key] = data[key].replace(',', '.')

            # Validación y conversión de valores a Decimal
            try:
                presupuesto = Decimal(data.get('presupuesto'))
                transporte = Decimal(data.get('transporte'))
                personal = Decimal(data.get('personal'))
                combustible = Decimal(data.get('combustible'))
                alquiler = Decimal(data.get('alquiler'))
                viaticos = Decimal(data.get('viaticos'))
                donaciones = Decimal(data.get('donaciones'))
                otros = Decimal(data.get('otros'))

                # Calcula el totalgastado y residuo
                totalgastado = presupuesto - (transporte + personal + combustible + alquiler + viaticos + donaciones + otros)
                residuo = presupuesto - totalgastado

                # Asigna los valores calculados
                gasto_obj.presupuesto = presupuesto
                gasto_obj.transporte = transporte
                gasto_obj.personal = personal
                gasto_obj.combustible = combustible
                gasto_obj.alquiler = alquiler
                gasto_obj.viaticos = viaticos
                gasto_obj.donaciones = donaciones
                gasto_obj.otros = otros
                gasto_obj.totalgastado = totalgastado
                gasto_obj.residuo = residuo
            except Exception as e:
                messages.error(request, 'Los valores ingresados deben ser numéricos.', extra_tags="danger")
                return redirect('gastos:list_gasto')

            gasto_obj.save()

            messages.success(request, 'Gasto actualizado con éxito!', extra_tags="success")
            return redirect('gastos:list_gasto')

        return render(request, "gasto/actualizar_gasto.html", {
            'gasto': gasto_obj,
            'eventos': eventos,
        })

    except gasto.DoesNotExist:
        messages.error(request, 'El gasto que intentas actualizar no existe.', extra_tags="danger")
        return redirect('gastos:list_gasto')
    except evento.DoesNotExist:
        messages.error(request, 'El evento asociado no existe.', extra_tags="danger")
        return redirect('gastos:list_gasto')
    except Exception as e:
        messages.error(request, 'Error al actualizar el gasto: ' + str(e), extra_tags="danger")
        return redirect('gastos:list_gasto')