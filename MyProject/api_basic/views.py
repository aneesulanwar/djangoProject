from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Article,sportArticle,applicationUser
from .serializer import ArticleSerializer, SportArticleSerializer,UserSerializer, RegisterSerializer,appUserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer1 = appUserSerializer(data=request.data)
    
        #if not user1 is None:
        if serializer1.is_valid(raise_exception=True):
            #data = serializer1.validated_data['username']
            #user1 = appUser.objects.get(username=data)
            serializer1.save()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data
        #"token": Token.objects.create(user)[1]
        })


class UserDetailAPI(APIView):
    serializerc= appUserSerializer
    def get_object(self,username):
        try:
            return applicationUser.objects.get(username=username)
        except applicationUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,*args,**kwargs):
        user = applicationUser.objects.get(username=self.request.GET.get('username'))
        serializer = appUserSerializer(user)
        return Response(serializer.data)
        


class UserApiView(APIView):
    def post(self,request):
         serializer = appUserSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleApiView(APIView):

    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    def post(self,request):
         serializer = ArticleSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    def get_object(self,title):
        try:
            return Article.objects.get(title=title)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,title):
        article = self.get_object(title)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request,title):
        article = self.get_object(title)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,title):
        article = self.get_object(title)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##

class sportArticleApiView(APIView):

    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        articles = sportArticle.objects.all()
        serializer = SportArticleSerializer(articles,many=True)
        return Response(serializer.data)

    def post(self,request):
         serializer = SportArticleSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class sportArticleDetails(APIView):
    def get_object(self,title):
        try:
            return sportArticle.objects.get(title=title)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,title):
        article = self.get_object(title)
        serializer = SportArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request,title):
        article = self.get_object(title)
        serializer = SportArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,title):
        article = self.get_object(title)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##


@api_view(['GET','POST'])
def login(request):
    
    if request.method == 'POST':
        
        body_unicode = request.body.decode('utf-8')
        #body = JSONParser().parse(body_unicode)
        #content = body['username']
        return Response(body_unicode, status=status.HTTP_201_CREATED)
        



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
        return Response(serializer.data)

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


@api_view(['GET','PUT','DELETE'])
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
