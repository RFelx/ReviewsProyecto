from api_main_core.serializers.productora_serializer import ProductoraSerializer
from rest_framework import viewsets
from review_app.models import Productora
class ProductoraViewSet(viewsets.ModelViewSet):
    queryset = Productora.objects.all()
    serializer_class = ProductoraSerializer