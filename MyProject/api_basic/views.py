from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article,sportArticle
from .serializer import ArticleSerializer, SportArticleSerializer
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET','POST'])
def articles(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def sportArticles(request):
    if request.method == 'GET':
        articles = sportArticle.objects.all()
        serializer = SportArticleSerializer(articles,many=True)
        return Response(serializer.data,safe=False)

    if request.method == 'POST':
    
        serializer = SportArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def articlesDetails(request,title):
    try:
        article = Article.objects.get(title=title)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "Delete":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def sportsDetails(request,title):
    try:
        article = sportArticle.objects.get(title=title)
    except sportArticle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = SportArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
    
        serializer = SportArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "Delete":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# Create your views here.
