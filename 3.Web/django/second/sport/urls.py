from django.conf.urls import url
from .views import *
#访问路径是http://localhost:8000/sport/***
#要交给当前的urls.py去处理
urlpatterns = [
    #访问路径是http://localhost:8000/sport/index
    url(r'^index/$',index_views),
]