from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Image, News, Category, Comment



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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('news_pk', 'topics')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','author' ,'title' ,'sentiment','trending', 'summary', 'like', 'full_url', 'publishedDate')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'news')
