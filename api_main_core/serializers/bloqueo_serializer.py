from review_app.models import Bloqueo
from rest_framework import serializers

class BloqueoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bloqueo
        fields = ["bloqueador","bloqueado"]