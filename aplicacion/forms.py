from django import forms
from .models import Usados, Nuevos, Service, Administracion, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserEditForm(UserCreationForm):
    email =forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label= "Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la Contraseña",widget=forms.PasswordInput)
    first_name = forms.CharField(label= "Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label= "Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1',"password2"]
        help_texts = {k:"" for k in fields}


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)