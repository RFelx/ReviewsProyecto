from api_main_core.serializers.comentario_serializer import ComentarioSerializer
from rest_framework import viewsets
from review_app.models import Comentario
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
