from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class applicationUser(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class sportArticle(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    data = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class articleLikes(models.Model):
    username = models.CharField(max_length=100)
    articleId = models.IntegerField()
    def __str__(self):
        return self.articleId


class articleComments(models.Model):
    username = models.CharField(max_length=100)
    articleId = models.IntegerField()
    comment = models.TextField()
    def __str__(self):
        return self.comment


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
    