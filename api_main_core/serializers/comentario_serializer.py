from review_app.models import Comentario
from rest_framework import serializers

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ["user","review","comentario","fecha"]