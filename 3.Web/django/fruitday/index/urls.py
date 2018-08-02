from django.conf.urls import url
from .views import *

urlpatterns = [
    #访问http://localhost:8000/login/交给login_views处理
    url(r'^login/$',login_views,name="login"),
    #访问http://localhost:8000/register/
    url(r'^register/$',register_views,name="reg"),
]