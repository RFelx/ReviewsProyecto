from review_app.models import Contenido
from rest_framework import serializers

class ContenidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contenido
        fields = ["nombre","categoria","fecha_estreno","escritor","productora"]