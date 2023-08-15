from django.urls import path, include
from .views import nuevos,usados,index,administracion,service,usadoFormf
from .models import *
from . import views

urlpatterns = [
    path('', index, name="inicio" ),
    path('service/', service, name='service'),
    path('nuevos/', nuevos , name='nuevos'),
    path('usados/', usados , name='usados'),
    path('administracion/', administracion, name='administracion'),

    path('usadoForm/', usadoFormf, name='usadoForm'),


]
