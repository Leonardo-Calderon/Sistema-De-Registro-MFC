from django.shortcuts import render, redirect
from cliente.models import DatosPersonales, Dispositivo
from cliente.forms import FormDatos
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404

SUCCESS = 25

def lista_clientes(request):
    paginate_by = 5
    datos = DatosPersonales.objects.all()
    len(datos)
    DatosPersonales.objects.count()

    
    return render(request, 'datos.html', {'datos': datos})

def eliminar_cliente(request, id):
    DatosPersonales.objects.get(id=id).delete()
    messages.add_message(request, SUCCESS, 'Se elimino correctamente')
    return redirect('cliente_lista')

def nuevo_cliente(request):
    if request.method == 'POST':
        form = FormDatos(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, SUCCESS, 'Se creo correctamente')
            return redirect('cliente_lista')
    else:
        form = FormDatos()
    return render(request, 'nuevo_cliente.html', {'form':form})

def editar_cliente(request, id):
    datos = DatosPersonales.objects.get(id=id)
    if request.method == 'POST':
        form = FormDatos(request.POST, instance=datos)
        if form.is_valid():
            form.save()
            messages.add_message(request, SUCCESS, 'Se edito correctamente')
            return redirect('cliente_lista')
    else:
        form = FormDatos(instance=datos)
    return render(request, 'editar_cliente.html', {'form':form})

