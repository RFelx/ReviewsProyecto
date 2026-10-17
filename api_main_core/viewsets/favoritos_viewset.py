from api_main_core.serializers.favoritos_serializer import FavoritoSerializer
from rest_framework import viewsets
from review_app.models import Favoritos
class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritoSerializer
