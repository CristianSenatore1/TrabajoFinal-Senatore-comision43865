from django import forms
from .models import Contacto, Usados, Nuevos, Service, Administracion

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class UsadoForm(forms.ModelForm):
    class Meta:
        model = Usados
        fields = '__all__'
    
class NuevoForm(forms.ModelForm):
    class Meta:
        model = Nuevos
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class AdministracionForm(forms.ModelForm):
    class Meta:
        model = Administracion
        fields = '__all__'
