from django.contrib import admin
from .models import (
    UserProfile, 
    Escritor, 
    Productora, 
    Contenido, 
    Review, 
    Comentario, 
    Favoritos, 
    Seguir, 
    Bloqueo
)
admin.site.register(UserProfile)
admin.site.register(Escritor)
admin.site.register(Productora)
admin.site.register(Contenido)
admin.site.register(Review)
admin.site.register(Comentario)
admin.site.register(Favoritos)
admin.site.register(Seguir)
admin.site.register(Bloqueo)