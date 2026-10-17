from review_app.models import Escritor
from rest_framework import serializers

class EscritorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escritor
        fields = ["bio","nombre"]

