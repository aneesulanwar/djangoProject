from rest_framework import serializers
from .models import Article,sportArticle,applicationUser
from django.contrib.auth.models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'], validated_data['password'])
        return user


class appUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = applicationUser
        fields = ['username', 'first_name','last_name','email', 'date']


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id','title','author','email','date']


class SportArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = sportArticle
        fields = ['id','title','author','email','data','date']





'''
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self,validated_data):
        return Article.objects.create(validated_data)

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.author = validated_data.get('author',instance.author)
        instance.email = validated_data.get('email',instance.email)
        instance.date = validated_data.get('date',instance.date)

'''

'''

class SportArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    data = serializers.TextField(max_length=1000)
    date = serializers.DateTimeField()

    def create(self,validated_data):
        return sportArticle.objects.create(validated_data)
'''