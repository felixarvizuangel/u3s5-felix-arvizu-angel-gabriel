# models: trae las herramientas de Django para describir tablas como clases
from django.db import models
# User: el modelo de usuario que Django ya trae incluido (login, contraseñas, sesiones)
from django.contrib.auth.models import User

# class Servicio: se convierte en la tabla "core_servicio" dentro de MySQL
class Servicio(models.Model):
    # propietario: relaciona este servicio con el usuario dueño
    # on_delete=CASCADE: si se borra ese usuario, se borran también sus servicios
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    # titulo: texto corto y obligatorio, máximo 120 caracteres
    titulo = models.CharField(max_length=120)

    # descripcion: texto largo, sin límite fijo de caracteres
    descripcion = models.TextField()

    # precio: número decimal — hasta 8 dígitos en total, 2 después del punto (ej. 1500.00)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    # categoria: texto corto para clasificar el servicio (ej. "Tutorías", "Diseño")
    categoria = models.CharField(max_length=60)

    # creado_en: Django guarda automáticamente la fecha y hora cuando se crea el registro
    creado_en = models.DateTimeField(auto_now_add=True)

    # disponible: indica si el servicio está activo (coincide con la migración 0002)
    disponible = models.BooleanField(default=True)

    # __str__: define qué texto se muestra al "imprimir" este objeto (ej. en el panel /admin)
    def __str__(self):
        # f-string: arma un texto con el título, un guion y el precio del objeto
        return f"{self.titulo} — ${self.precio}"
