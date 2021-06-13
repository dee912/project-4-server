from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from server.serializer import StoreSerializer

User = get_user_model()

class PopulatedSerializer(ModelSerializer):
    faviourites = StoreSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image', 'email')
