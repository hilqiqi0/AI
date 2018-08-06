from django.conf.urls import url
from django.contrib import admin
from userinfo import views

urlpatterns = [
    url('^register/',views.register_in,name='register'),
    url('^registerin/',views.register_,name='register_in'),
    url('^login/',views.login_in,name='login'),
    url('^loginin/',views.login_,name='login_in'),
    url('^loginout/',views.login_out,name='login_out'),


]