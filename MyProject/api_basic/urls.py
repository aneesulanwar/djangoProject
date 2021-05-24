from django.urls import path
from .views import articles,sportArticles,articlesDetails, sportsDetails

urlpatterns = [
    path('articles/', articles),
    path('sport-articles/', sportArticles),
    path('articles-details/<str:title>/',articlesDetails),
    path('sports-details/<str:title>/',sportsDetails)
]