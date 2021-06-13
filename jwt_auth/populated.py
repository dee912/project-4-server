from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from server.serializer import StoreSerializer, CommentSerializer

User = get_user_model()

class PopulatedUserSerializer(ModelSerializer):
    favourites = StoreSerializer(many=True)
    comments = CommentSerializer(many=True)
    owned_stores = StoreSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'profile_image',
            'email',
            'favourites',
            'comments',
            'owned_stores'
        )
