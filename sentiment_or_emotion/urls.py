from django.urls import path
#from django.conf.urls import url
from . import views

app_name = 'sentiment_or_emotion'

from sentiment_or_emotion.views import choose_sentiment_or_emotion

urlpatterns = [
    path('', choose_sentiment_or_emotion, name="choose_sentiment_or_emotion"),
]

# urlpatterns = [
#     path(r'', views.choose_sentiment_or_emotion, name="choose_sentiment_or_emotion"),
# ]