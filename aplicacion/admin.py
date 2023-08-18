from django.contrib import admin
from .models import Administracion, Service, Nuevos, Usados, Contacto, Avatar

# Register your models here.
admin.site.register(Administracion)
admin.site.register(Service)
admin.site.register(Nuevos)
admin.site.register(Usados)
admin.site.register(Contacto)
admin.site.register(Avatar)
