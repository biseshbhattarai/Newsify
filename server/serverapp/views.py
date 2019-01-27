from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, NewsSerializer, CategorySerializer, CommentSerializer
import requests
from bs4 import BeautifulSoup
from rest_framework.permissions import IsAuthenticated
from .models import News, Category, Comment
import json
from textblob import TextBlob
from rest_framework.decorators import api_view
import random
from . import sentiment_mod as s
from rest_framework import serializers




API_KEY = 'dbd603ed45954a108748fc3e88bfda7d'

class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommentList(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class NewsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CategoryView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


def filter_topics(request):
    news = News.objects.all()
    all_words = []
    for itr in news:
        print(itr.summary)
        if itr.summary != None:
            extract = TextBlob(itr.summary)
            noun_words = extract.noun_phrases
            if len(noun_words) != 0:
                all_words.append(len(noun_words))
                noun_word = noun_words[random.randrange(0, len(noun_words))]
                root = Category()
                root.news_pk = itr.id
                noun_word = noun_words[random.randrange(len(noun_words))]
                root.topics = noun_word
                root.save()


@api_view(['POST'])
def like(request, pk=None):
    if request.method == 'POST':
       news = News.objects.get(pk=pk)
       news.like += 1
       news.save()
       
       return Response(news.like)


class FetchView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        res = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey='+ API_KEY)
        if res.status_code == 200:
            for  i in res.json()['articles']:
                root = News()
                root.trending = True
                root.title = i['title']
                root.summary = i['description']
                root.full_url = i['url']
                root.publishedDate = i['publishedAt']
                root.author = i['author']
                print(i['title'])

                data = s.sentiment(i['title'])[0]
                print(data)
                root.sentiment = data
                root.save()
        filter_topics(request)
        return Response('FETCHED AND SAVED')
 

class CurrentUser(APIView):

    def get(self, request):
        user = request.user.username
        return Response(user)
