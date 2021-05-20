from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article,sportArticle
from .serializer import ArticleSerializer, SportArticleSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def articles(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


# Create your views here.
