from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Avatar, Nuevos ,Usados ,Service , Administracion
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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
class NuevosList(LoginRequiredMixin,ListView):
    model = Nuevos
class UsadosList(LoginRequiredMixin,ListView):
    model = Usados
class ServiceList(LoginRequiredMixin,ListView):
    model = Service
class AdministracionList(LoginRequiredMixin,ListView):
    model = Administracion
#----------------------
class UsadosCreate(LoginRequiredMixin,CreateView):
    model = Usados
    fields = '__all__'
    success_url = reverse_lazy('usados')
class NuevosCreate(LoginRequiredMixin,CreateView):
    model = Nuevos
    fields = '__all__'
    success_url = reverse_lazy('nuevos')
class ServiceCreate(LoginRequiredMixin,CreateView):
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('service')
class AdministracionCreate(LoginRequiredMixin,CreateView):
    model = Administracion
    fields = '__all__'
    success_url = reverse_lazy('administracion')
#----------------------
class ServiceDetail(LoginRequiredMixin,DetailView):
    model = Service
class NuevosDetail(LoginRequiredMixin,DetailView):
    model = Nuevos
class UsadosDetail(LoginRequiredMixin,DetailView):
    model = Usados
class AdministracionDetail(LoginRequiredMixin,DetailView):
    model = Administracion
#--------------------------------

class UsadosUpdate(LoginRequiredMixin,UpdateView):
    model = Usados
    fields = '__all__'
    success_url = reverse_lazy('usados')
class NuevosUpdate(LoginRequiredMixin,UpdateView):
    model = Nuevos
    fields = '__all__'
    success_url = reverse_lazy('nuevos')
class ServiceUpdate(LoginRequiredMixin,UpdateView):
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('service')
class AdministracionUpdate(LoginRequiredMixin,UpdateView):

    model = Administracion
    fields = '__all__'
    success_url = reverse_lazy('administracion')
#--------------------------------
class UsadosDelete(LoginRequiredMixin,DeleteView):
    model = Usados
    success_url = reverse_lazy('usados')
class NuevosDelete(LoginRequiredMixin,DeleteView):
    model = Nuevos
    success_url = reverse_lazy('nuevos')
class ServiceDelete(LoginRequiredMixin,DeleteView):
    model = Service
    success_url = reverse_lazy('service')
class AdministracionDelete(LoginRequiredMixin,DeleteView):
    model = Administracion
    success_url = reverse_lazy('administracion')
#--------------------------------

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, 'aplicacion/base.html',{"mensaje":f"Bienvenido{usuario}"})
            else:
                return render(request, 'aplicacion/login.html',{"form":miForm,"mensaje":"Datos Inválidos"})
        else:
            return render(request, 'aplicacion/login.html',{"form":miForm,"mensaje":"Datos Inválidos"})
        
    miForm = AuthenticationForm()
    return render (request, 'aplicacion/login.html',{"form":miForm})

def register (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            form.save()
            return render(request, "aplicacion/base.html",{"mensaje":"Usuario creado con Exito"})
    else:
        form = UserCreationForm()

    return render (request, 'aplicacion/registro.html',{"form":form})


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje':f"Usuario{usuario.username} actualizado correctamente"})
        else:
            return render(request,"aplicacion/editarPerfil.html",{'form':form})
    else:
        form = UserEditForm(instance=usuario)
    return render (request, "aplicacion/editarPerfil.html",{'form':form, 'usuario':usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
            return render(request,"aplicacion/editarPerfil.html",{'form':form})
    else:
        form = AvatarFormulario()
    return render (request, "aplicacion/agregarAvatar.html",{'form':form})
