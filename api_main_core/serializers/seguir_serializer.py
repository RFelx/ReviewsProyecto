from review_app.models import Seguir
from rest_framework import serializers

class SeguirSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seguir
        fields = ["seguidor","seguido"]