from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to='perfiles/', default='image/usuario.png', blank=True, null=True)

class Escritor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='escritores/', default='image/usuario.png', blank=True, null=True)
    def __str__(self):
            return self.nombre

class Productora(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    fecha_creacion = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='productoras/', default='image/usuario.png', blank=True, null=True)
    def __str__(self):
        return self.nombre

class Contenido(models.Model):  
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    fecha_estreno = models.DateField(null=True, blank=True)
    escritor = models.ForeignKey(Escritor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Escritor")
    productora = models.ForeignKey(Productora, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Productora")
    imagen = models.ImageField(upload_to='contenidos/', default='image/usuario.png', blank=True, null=True)
    def __str__(self):
        return self.nombre

class Review(models.Model):
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    argumento = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    score = models.DecimalField(max_digits =2,decimal_places=1)

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateField(auto_now_add=True)

class Favoritos(models.Model):
    user = models.ManyToManyField(User)
    contenido = models.ManyToManyField(Contenido)

class Bloqueo(models.Model):
    bloqueador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bloqueador')
    bloqueado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bloqueado')

class Seguir(models.Model):
    seguidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguidor')
    seguido = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguido')