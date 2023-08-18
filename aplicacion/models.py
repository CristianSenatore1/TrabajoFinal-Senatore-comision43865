from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nuevos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    combustible = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=20, decimal_places=0)

    def __str__(self):
        return f"{self.marca},{self.modelo}"

class Usados(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    kilometraje = models.PositiveBigIntegerField()
    precio = models.DecimalField(max_digits=20, decimal_places=0 ) 

    def __str__(self):
        return f"{self.marca},{self.modelo}"

class Administracion(models.Model):
    cliente = models.CharField(max_length=50)
    estado_de_documentacion = models.CharField(max_length=50)
    financiacion = models.CharField(max_length=50)
    proximo_paso = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cliente}, proximo paso = {self.proximo_paso}"


class Service (models.Model):
    cliente = models.CharField(max_length=50)
    turnos = models.DateField(max_length=50)
    mantenimiento = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.cliente},fecha turno = {self.turnos}, service de kms = {self.mantenimiento}"



class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}[{self.imagen}]"