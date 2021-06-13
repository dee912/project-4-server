from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Store, Category, Comment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

#! Populated

class PopulatedCommentSerializer(CommentSerializer):
    owner = UserSerializer()

class PopulatedStoreSerializer(StoreSerializer):
    category = CategorySerializer(many=True)
    comments = PopulatedCommentSerializer(many=True)
    favourites = UserSerializer(many=True)
