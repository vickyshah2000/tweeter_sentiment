"""sentiment_emotion_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('sentiment.urls')),
    path('', include('sentiment_or_emotion.urls')),
    path('', include('emotion.urls')),
  
]
# app_name= 'sentiment'
# from sentiment.views import sentiment_analysis
# from sentiment.views import sentiment_analysis_type
# from sentiment.views import sentiment_analysis_import


# urlpatterns = [
    
#     path('sentiment', sentiment_analysis, name="sentiment_anaylsis"),
#     path('', sentiment_analysis_type, name="sentiment_analysis_type"),
#     path('', sentiment_analysis_import, name="sentiment_analysis_import"),
# ]
# app_name='emotion'
# from emotion import views

# urlpatterns = [
#     path(r'', views.emotion_analysis, name="emotion_anaylsis"),
#     path(r'', views.emotion_analysis_type, name="emotion_analysis_type"),
#     path(r'', views.emotion_analysis_import, name="emotion_analysis_import"),
# ]

# app_name='sentiment_or_emotion'
# from sentiment_or_emotion import views

# urlpatterns = [
#     path(r'', views.choose_sentiment_or_emotion, name="choose_sentiment_or_emotion"),
#     #path('sentiment/import', views.import_sentiment_data, name='import_sentiment_data'),

# ]
