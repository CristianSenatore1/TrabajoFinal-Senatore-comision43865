from django.contrib import admin
from .models import Administracion, Service, Nuevos, Usados

# Register your models here.
admin.site.register(Administracion)
admin.site.register(Service)
admin.site.register(Nuevos)
admin.site.register(Usados)
# admin.site.register(Contacto)
