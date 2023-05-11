from django.urls import path
#from django.conf.urls import url
from . import views


# urlpatterns = [
#     path(r'', views.emotion_analysis, name="emotion_anaylsis"),
#     path(r'', views.emotion_analysis_type, name="emotion_analysis_type"),
#     path(r'', views.emotion_analysis_import, name="emotion_analysis_import"),
# ]

# urlpatterns = [
#     path(r'<str:emotion_type>', views.emotion_analysis_type, name='emotion_analysis_type'),
#     path(r'import', views.emotion_analysis_import, name='emotion_analysis_import'),
    

# ]
app_name = 'emotion'

from emotion.views import emotion_analysis
from emotion.views import emotion_analysis_type
from emotion.views import emotion_analysis_import

urlpatterns = [

    path('emotion', emotion_analysis, name="emotion_analysis"),
    path('emotion/type/', emotion_analysis_type, name="emotion_analysis_type"),
    path('emotion/import/', emotion_analysis_import, name="emotion_analysis_import"),

]
