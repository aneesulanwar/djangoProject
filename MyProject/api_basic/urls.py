from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import articles,sportArticles,articlesDetails,sportArticleApiView,UserDetailAPI ,sportsDetails,UserApiView ,ArticleApiView,ArticleDetails,RegisterAPI

urlpatterns = [
    path('articles/', ArticleApiView.as_view()),
    path('sport-articles/', sportArticleApiView.as_view()),
    path('articles-details/<str:title>/',ArticleDetails.as_view()),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('sports-details/<str:title>/',sportsDetails),
    path('users-details/', UserDetailAPI.as_view()),
    path('login/',obtain_auth_token),

]