from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, NewsSerializer
import requests
from bs4 import BeautifulSoup
from rest_framework.permissions import IsAuthenticated
from .models import News
import json
from textblob import TextBlob
from rest_framework.decorators import api_view
import random




API_KEY = 'dbd603ed45954a108748fc3e88bfda7d'





class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = News.objects.all()
    serializer_class = NewsSerializer


       

class CategoryView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        news = News.objects.all()
        all_words = []
        for itr in news:
            extract = TextBlob(itr.summary)
            noun_words = extract.noun_phrases
            noun_word = noun_words[random.randrange(len(noun_words))]
            all_words.append(noun_word)
            
        return Response(all_words)

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
                root.full_news = i['content']
                root.save()
        return redirect('/news')
 

