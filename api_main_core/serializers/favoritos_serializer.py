from review_app.models import Favoritos
from rest_framework import serializers

class FavoritoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favoritos
        fields = ["user","contenido"]