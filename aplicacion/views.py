from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Nuevos ,Usados ,Service , Administracion
from .forms import ContactoForm

def index(request):
    return render(request, "aplicacion/base.html")

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

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('formulario_contacto')
    else:
        form = ContactoForm()

    return render(request, 'aplicacion/contactoForm.html',{'form':form})
    