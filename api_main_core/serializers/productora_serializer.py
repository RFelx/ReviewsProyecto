from review_app.models import Productora
from rest_framework import serializers

class ProductoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productora
        fields = ["bio","nombre"]