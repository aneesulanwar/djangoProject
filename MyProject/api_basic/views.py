from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

# Create your views here.
