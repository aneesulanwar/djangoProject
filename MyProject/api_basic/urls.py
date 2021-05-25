from django.urls import path
from .views import articles,sportArticles,articlesDetails, sportsDetails, ArticleApiView,ArticleDetails

urlpatterns = [
    path('articles/', ArticleApiView.as_view()),
    path('sport-articles/', sportArticles),
    path('articles-details/<str:title>/',ArticleDetails.as_view()),
    path('sports-details/<str:title>/',sportsDetails)
]