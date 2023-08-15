from django import forms
from .models import Contacto, Usados 

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class UsadoForm(forms.ModelForm):

    class Meta:
        model = Usados
        fields = '__all__'
    
