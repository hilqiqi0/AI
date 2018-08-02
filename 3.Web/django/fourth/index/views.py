from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.
def request_views(request):
    # print(dir(request))
    # return HttpResponse('Response OK')

    scheme = request.scheme
    body = request.body
    host = request.get_host()
    path = request.path
    method = request.method
    get = request.GET
    post = request.POST
    cookies = request.COOKIES
    return render(request,'01_request.html',locals())

def login_views(request):
    if request.method == 'GET':
        return render(request,'02_login.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        return HttpResponse('用户名:'+uname+',密码:'+upwd)

def get_views(request):

    # if 'uname' in request.GET:
    #     uname = request.GET['uname']
    # if 'upwd' in request.GET:
    #     upwd = request.GET['upwd']

    uname = request.GET.get('uname','')
    upwd = request.GET.get('upwd','')


    if uname and upwd:
        return HttpResponse('用户名:'+uname+",密码:"+upwd)
    else:
        return render(request,'03_login.html')

def query_views(request):
    id = request.GET.get('id','')
    name = request.GET.get('name','')

    return HttpResponse('id:'+id+',name:'+name)


def form_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request,'04_form.html',locals())
    else:
        #　1.将request.POST的数据交给RemarkForm()
        form = RemarkForm(request.POST)
        # 2.验证数据是否都符合规范(必须要通过验证)
        if form.is_valid():
            # 3.通过验证后，再通过cleaned_data取值
            cd = form.cleaned_data
            return HttpResponse(cd['subject']+','+cd['email'])

def register_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'05_register.html',locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            users = Users(**cd)
            users.save()
            return HttpResponse('Register OK')

def modelForm_views(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'06_login.html',locals())


def addCookie_views(request):
    # 不使用模板
    # resp = HttpResponse('添加cookie成功')
    # resp.set_cookie('uname1','zsf',60*60*24)
    # return resp

    # 使用模板
    # resp = render(request,'07_setcookie.html',locals())
    # resp.set_cookie('uname2','zhangwuji',60*60*24*31)
    # return resp

    #使用重定向
    resp = HttpResponseRedirect('/03_get/')
    resp.set_cookie('uname3','zhaomin',60*60*24*366)
    return resp

def getCookie_views(request):
    cookies=request.COOKIES
    print(cookies)
    return HttpResponse('Get Cookies OK')

def setSession_views(request):
    uname = 'sanfeng.zhang'
    uemail = 'sf.zh@163.com'
    #将以上两个数据保存进session
    request.session['uname']=uname
    request.session['uemail']=uemail
    return HttpResponse('Add Session Success!')

def getSession_views(request):
    uname = request.session.get('uname')
    uemail = request.session.get('uemail')
    return HttpResponse('uname:'+uname+',uemail:'+uemail)