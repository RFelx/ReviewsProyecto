from api_main_core.serializers.bloqueo_serializer import BloqueoSerializer
from rest_framework import viewsets
from review_app.models import Bloqueo
class BloqueoViewSet(viewsets.ModelViewSet):
    queryset = Bloqueo.objects.all()
    serializer_class = BloqueoSerializer
