from review_app.models import UserProfile
from rest_framework import serializers

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["bio","nombre"]

