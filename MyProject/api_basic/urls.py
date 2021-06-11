from django.urls import path
from .views import articles,sportArticles,articlesDetails, sportsDetails,UserApiView ,ArticleApiView,ArticleDetails,RegisterAPI

urlpatterns = [
    path('articles/', ArticleApiView.as_view()),
    path('sport-articles/', sportArticles),
    path('articles-details/<str:title>/',ArticleDetails.as_view()),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('sports-details/<str:title>/',sportsDetails)
]