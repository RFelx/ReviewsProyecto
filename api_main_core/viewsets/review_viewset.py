from api_main_core.serializers.review_serializers import ReviewSerializer
from rest_framework import viewsets
from review_app.models import Review
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
