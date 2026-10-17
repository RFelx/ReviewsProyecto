from api_main_core.serializers.seguir_serializer import SeguirSerializer
from rest_framework import viewsets
from review_app.models import Seguir
class SeguirViewSet(viewsets.ModelViewSet):
    queryset = Seguir.objects.all()
    serializer_class = SeguirSerializer
