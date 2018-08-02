from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def login_views(request):
    if request.method == 'GET':
        # 判断cookies中是否有id 和　uphone
        if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
            return HttpResponse('欢迎:'+request.COOKIES['uphone']+'回来!')
        else:
            form = LoginForm()
            return render(request, 'login.html', locals())
    else:
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']

        users = Users.objects.filter(uphone=uphone, upwd=upwd)
        if users:
            resp = HttpResponse('登录成功!')
            # 是否记住密码
            if 'isSaved' in request.POST:
                MAX_AGE=60*60*24*366
                resp.set_cookie('id',users[0].id,MAX_AGE)
                resp.set_cookie('uphone',uphone,MAX_AGE)

            return resp
        else:
            form = LoginForm()
            return render(request,'login.html',locals())



def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 接收用户的手机号,判断号码是否存在
        uphone = request.POST['uphone']
        users = Users.objects.filter(uphone=uphone)
        if users:
            # 手机号已经注册过，给出提示，回到注册页面
            errMsg = '手机号码已经注册'
            return render(request, 'register.html', locals())
        else:
            upwd = request.POST['upwd']
            uname = request.POST['uname']
            uemail = request.POST['uemail']

            Users.objects.create(uphone=uphone,
                                 upwd=upwd, uname=uname, uemail=uemail)
            return HttpResponse('注册成功!')
