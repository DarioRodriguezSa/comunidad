from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import  nacionalidad, estadocivil, genero
from .models import miembro
from django.contrib.auth.decorators import login_required





@login_required(login_url="auth/login/")

def agregar_miembros(request):
    nacionalidades = nacionalidad.objects.all()
    estadociviles = estadocivil.objects.all()
    generos = genero.objects.all()

    if request.method == 'POST':
        data = request.POST
        nombre = data['nombre']
        apellidos = data['apellidos']
        di = data['id']

        try:
            miembro_existente = miembro.objects.get(nombre=nombre, apellido=apellidos)
            messages.error(request, 'Ya existe un miembro con los mismos nombres y apellidos.', extra_tags="danger")
            return redirect('miembros:agregar_miembro')
        except miembro.DoesNotExist:
            pass

        try:
            miembro_existente = miembro.objects.get(di=di)
            messages.error(request, 'Ya existe un miembro con el mismo ID.', extra_tags="danger")
            return redirect('miembros:agregar_miembro')
        except miembro.DoesNotExist:
            pass

        try:
            nacionalidad_obj = nacionalidad.objects.get(pk=data['nacionalidad'])
            estadocivil_obj = estadocivil.objects.get(pk=data['estadocivil'])
            genero_obj = genero.objects.get(pk=data['genero'])

            nuevo_miembro = miembro(
                nombre=nombre,
                apellido=apellidos,
                edad=data['edad'],
                nacionalidad=nacionalidad_obj,
                estadocivil=estadocivil_obj,
                genero=genero_obj,
                di=di,
                direccion=data['direccion'],
                telefono=data['telefono'],
                correo=data['correo'],
                nohijos=data['num_hijos']
            )
            nuevo_miembro.save()

            messages.success(request, 'Miembro creado con éxito!', extra_tags="success")
            return redirect('miembros:agregar_miembro')

        except Exception as e:
            messages.error(request, 'Error al crear el miembro: ' + str(e), extra_tags="danger")
            return redirect('miembros:agregar_miembro')

    return render(request, "miembro/miembros.html", {'nacionalidades': nacionalidades, 'estadosciviles': estadociviles, 'generos': generos})


def listar_m(request):
    query = request.GET.get('q', '')
    miembros_list = miembro.objects.filter(
        Q(nombre__icontains=query) |
        Q(di__icontains=query) |
        Q(genero__nombre__icontains=query) |
        Q(nacionalidad__nombre__icontains=query) |
        Q(estadocivil__nombre__icontains=query) |
        Q(edad__icontains=query)
    )
    context = {
        "active_icon": "miembros",
        "miembros": miembros_list,
        "query": query,
    }
    return render(request, "miembro/listar_miembros.html", context)







@login_required(login_url="auth/login/")
def eliminar_miembros(request, miembro_id):
    try:
        Miembro = miembro.objects.get(pk=miembro_id)
        Miembro.delete()
        messages.success(request, '¡Miembro eliminado!', extra_tags="success")
        return redirect('miembros:lista_miembro')  
    except Exception as e:
        messages.error(request, '¡Hubo un error durante la eliminación!' + str(e), extra_tags="danger")
        return redirect('miembros:lista_miembro')
    



@login_required(login_url="auth/login/")
def actualizar_miembro(request, miembro_id):
    try:
        Miembro = miembro.objects.get(id=miembro_id)
        nacionalidades = nacionalidad.objects.all()
        estadociviles = estadocivil.objects.all()
        generos = genero.objects.all()
        context = {
            'nacionalidades': nacionalidades,
            'estadosciviles': estadociviles,
            'generos': generos,
            'miembro': Miembro,  # Pasar el objeto Miembro
        }

        if request.method == 'POST':
            data = request.POST

            # Actualiza los campos del objeto Miembro
            Miembro.nombre = data['nombre']
            Miembro.apellido = data['apellidos']
            Miembro.edad = data['edad']
            Miembro.nacionalidad = nacionalidad.objects.get(pk=data['nacionalidad'])
            Miembro.estadocivil = estadocivil.objects.get(pk=data['estadocivil'])
            Miembro.genero = genero.objects.get(pk=data['genero'])
            nuevo_di = data['id']
            if nuevo_di != Miembro.di:
                # El DI ha cambiado, verificar si ya existe
                if miembro.objects.filter(di=nuevo_di).exclude(id=miembro_id).exists():
                    messages.error(request, 'Ya existe un miembro con el mismo DI.', extra_tags="danger")
                    return render(request, 'miembro/actualizar_miembros.html', context=context)
                
            if miembro.objects.filter(nombre=data['nombre'], apellido=data['apellidos']).exclude(id=miembro_id).exists():
                messages.error(request, 'Ya existe un miembro con el mismo nombre y apellido.', extra_tags="danger")
                return render(request, 'miembro/actualizar_miembros.html', context=context)


            Miembro.di = nuevo_di
            Miembro.direccion = data['direccion']
            Miembro.telefono = data['telefono']
            Miembro.correo = data['correo']
            Miembro.nohijos = data['num_hijos']

            # Guarda los cambios
            Miembro.save()

            messages.success(request, 'Miembro actualizado con éxito!', extra_tags="success")

            return redirect('miembros:lista_miembro')  # Redirige a la lista de miembros después de actualizar

        return render(request, 'miembro/actualizar_miembros.html', context=context)

    except miembro.DoesNotExist:
        messages.error(request, 'El miembro no existe', extra_tags="danger")
        return redirect('miembros:lista_miembro')

    except Exception as e:
        messages.error(request, '¡Hubo un error durante la actualización: ' + str(e), extra_tags="danger")
        return render(request, 'miembro/actualizar_miembros.html', context=context)
