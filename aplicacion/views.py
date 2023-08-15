from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Nuevos ,Usados ,Service , Administracion
from .forms import *

def index(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ContactoForm()

    return render(request, 'aplicacion/base.html',{'form':form})

def nuevos(request):
    nuevos_data = Nuevos.objects.all()
    ctx = {"autos":nuevos_data}
    return render(request, 'aplicacion/nuevos.html',ctx)

def usados(request):
    usados_data = Usados.objects.all()
    ctx = {"autos":usados_data}
    return render(request, 'aplicacion/usados.html',ctx)

def service (request):
    serv_info = Service.objects.all()
    ctx = {"autos":serv_info}
    return render(request, 'aplicacion/service.html',ctx)

def administracion(request):
    admin_data = Administracion.objects.all() 
    ctx = {"autos": admin_data}
    return render(request, 'aplicacion/administracion.html', ctx)

def usadoFormf(request):
    if request.method == 'POST':
        formUsado = UsadoForm(request.POST)
        if formUsado.is_valid():
            informacion = formUsado.cleaned_data
            usado = Usados(marca=informacion["marca"],modelo=informacion["modelo"],kilometraje=informacion["kilometraje"],precio=informacion["precio"])
            usado.save()
            return render(request, "aplicacion/base.html")
    else:
        formUsado = UsadoForm()
    
    return render ( request, "aplicacion/usadoForm.html",{ "form": formUsado }) 
