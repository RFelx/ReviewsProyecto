from api_main_core.serializers.userprofile_serializer import UserProfileSerializer
from rest_framework import viewsets
from review_app.models import UserProfile
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
