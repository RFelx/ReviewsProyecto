from api_main_core.serializers.escritor_serializer import EscritorSerializer
from rest_framework import viewsets
from review_app.models import Escritor
class EscritorViewSet(viewsets.ModelViewSet):
    queryset = Escritor.objects.all()
    serializer_class = EscritorSerializer
