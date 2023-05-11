from django.urls import path
#from django.conf.urls import url
from . import views

# app_name = 'sentiment'

# urlpatterns = [
#     path('', views.sentiment_analysis, name="sentiment_anaylsis"),
#     path('', views.sentiment_analysis_type, name="sentiment_analysis_type"),
#     path('', views.sentiment_analysis_import, name="sentiment_analysis_import"),
# ]


app_name= 'sentiment'
from sentiment.views import sentiment_analysis
from sentiment.views import sentiment_analysis_type
from sentiment.views import sentiment_analysis_import


urlpatterns = [
    
    path('sentiment', sentiment_analysis, name="sentiment_anaylsis"),
    path('sentiment/type/', sentiment_analysis_type, name="sentiment_analysis_type"),
    path('sentiment/import/', sentiment_analysis_import, name="sentiment_analysis_import"),
]