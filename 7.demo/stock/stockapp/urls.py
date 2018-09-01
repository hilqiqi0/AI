from django.conf.urls import url 
from stockapp.views import *

urlpatterns = [
    url(r'^index/$',index,name = 'index'),
    url(r'^(index)/realHead.html$',realHead),
    url(r'^company/(\d+)/realHead.html$',realHead),
    url(r'^.+/k.html$',k_line,name = 'k_line'),
    url(r'^login/$',do_login,name = 'login'),
    url(r'^reg/$',do_reg,name = 'register'),
    url(r'^logout/$', do_logout, name='logout'),
    url(r'^company/(\d{1,8})/$',company,name = 'company'),
    url(r'^account/$',account,name = 'account'),
    url(r'^add_optional/(\d{1,8})$',add_optional,name = 'add_optional')
]