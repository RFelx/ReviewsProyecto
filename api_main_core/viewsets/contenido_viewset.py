from api_main_core.serializers.contenido_serializer import ContenidoSerializer
from rest_framework import viewsets
from review_app.models import Contenido
class ContenidoViewSet(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer