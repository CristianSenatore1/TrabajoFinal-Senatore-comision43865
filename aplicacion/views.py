from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Nuevos ,Usados ,Service , Administracion
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

#-----------------------

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
class NuevosList(ListView):
    model = Nuevos
class UsadosList(ListView):
    model = Usados
class ServiceList(ListView):
    model = Service
class AdministracionList(ListView):
    model = Administracion
#----------------------
class UsadosCreate(CreateView):
    model = Usados
    fields = '__all__'
    success_url = reverse_lazy('usados')
class NuevosCreate(CreateView):
    model = Nuevos
    fields = '__all__'
    success_url = reverse_lazy('nuevos')
class ServiceCreate(CreateView):
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('service')
class AdministracionCreate(CreateView):
    model = Administracion
    fields = '__all__'
    success_url = reverse_lazy('administracion')
#----------------------
class ServiceDetail(DetailView):
    model = Service
class NuevosDetail(DetailView):
    model = Nuevos
class UsadosDetail(DetailView):
    model = Usados
class AdministracionDetail(DetailView):
    model = Administracion
#-------------------------------------

class UsadosUpdate(UpdateView):
    model = Usados
    fields = '__all__'
    success_url = reverse_lazy('usados')
class NuevosUpdate(UpdateView):
    model = Nuevos
    fields = '__all__'
    success_url = reverse_lazy('nuevos')
class ServiceUpdate(UpdateView):
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('service')
class AdministracionUpdate(UpdateView):

    model = Administracion
    fields = '__all__'
    success_url = reverse_lazy('administracion')
#--------------------------------
class UsadosDelete(DeleteView):
    model = Usados
    success_url = reverse_lazy('usados')
class NuevosDelete(DeleteView):
    model = Nuevos
    success_url = reverse_lazy('nuevos')
class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('service')
class AdministracionDelete(DeleteView):
    model = Administracion
    success_url = reverse_lazy('administracion')

