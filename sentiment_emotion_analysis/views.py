from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

def home(request):
    # Code to render the home page goes here
    return render(request, 'home/home.html')

# def sentiment_analysis(request):
#     # Your view code here
#     pass
