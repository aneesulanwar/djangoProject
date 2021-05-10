from django.urls import path
from .views import *
urlpatterns = [
    path('home',home,name='Home'),
    path('about',about,name='About'),
    path('contact',contact,name='Contact')
]