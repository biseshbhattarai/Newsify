from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Image, News



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(
            email = validated_data["email"],
            username = validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ('',)

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'trending', 'summary', 'full_news', 'like')