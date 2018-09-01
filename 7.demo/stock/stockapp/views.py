#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from stockapp.forms import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from stockapp.models import *
from stockapp.data import *

# Create your views here.

#主页
def index(request):
    is_login = request.user.is_authenticated()
    rank = Stock.objects.all()

    for i in rank:
        df = stock_company(i.number)
        setattr(i,'price',float(df.price[0]))
        setattr(i,'perce',"%.2f"%((float(df.price[0]) - float(df.pre_close)) / float(df.pre_close) * 100))

    ad = Link.objects.all()

    if is_login:
        login_user = request.user.username
        user = User.objects.get(username = login_user)
        optional = user.stock_set.all()
        for i in optional:
            df = stock_company(i.number)
            setattr(i,'price',float(df.price[0]))
            setattr(i,'perce',"%.2f"%((float(df.price[0]) - float(df.pre_close)) / float(df.pre_close) * 100))

    return render(request,'index.html',locals())

#头部数据调用
def realHead(request,template):
    if template == 'index':
        df = stock_A()
    else:
        df = stock_company(template)

    price = "%.2f"%(float(df.price[0]))
    open_price = "%.2f"%(float(df.open[0]))
    high = "%.2f"%(float(df.high[0]))
    low = "%.2f"%(float(df.low[0]))
    pre_close = "%.2f"%(float(df.pre_close[0]))
    volume = "%.2f"%(float(df.volume[0]) / 100000000)
    amount = "%.2f"%(float(df.amount[0]) / 100000000)
    change = "%.2f"%(float(price) - float(pre_close))
    perce = "%.2f"%(float(change) / float(pre_close) * 100)

    return render(request,'realHead.html',locals())

def k_line(request):
    k = ts.get_k_data('000001')
    return render(request,'k.html',locals())

#公司股票信息
def company(request,num):
    is_login = request.user.is_authenticated()
    rank = Stock.objects.all()
    for i in rank:
        df = stock_company(i.number)
        setattr(i,'price',float(df.price[0]))
        setattr(i,'perce',"%.2f"%((float(df.price[0]) - float(df.pre_close)) / float(df.pre_close) * 100))
    ad = Link.objects.all()

    if is_login:
        login_user = request.user.username
        user = User.objects.get(username = login_user)
        optional = user.stock_set.all()
        for i in optional:
            df = stock_company(i.number)
            setattr(i,'price',float(df.price[0]))
            setattr(i,'perce',"%.2f"%((float(df.price[0]) - float(df.pre_close)) / float(df.pre_close) * 100))
    if num == '0':
        num = request.POST['number']
        return redirect('/company/'+num)
    else:
        company = Stock.objects.get(number = num)
    return render(request,'company.html',locals())

@login_required
def add_optional(request,num):
    company = Stock.objects.get(number = num)
    company.user.add(request.user)
    return redirect(request.META.get('HTTP_REFERER','/'))

#个人账户
@login_required
def account(request):
    h = request.user.hold_set.all()
    hold_money = 0
    for i in h:
        hold_money += i.amount * float(stock_company(i.number).price[0])
    profit = 0
    for i in request.user.deal_set.all():
        profit += i.figure
    try:
        if request.method == 'POST':
            if request.POST['cmdType'] == 'buy':
                if Stock.objects.filter(number = int(request.POST['stockcode'])):
                    figure = int(request.POST['amount']) * float(stock_company(int(request.POST['stockcode'])).price[0])
                    user = User.objects.get(username = request.user.username)
                    user.money = user.money - figure
                    user.save()
                    dic = {'genre':0,'number':int(request.POST['stockcode']),'amount':int(request.POST['amount']),'figure':figure,'user':request.user}
                    obj = Deal(**dic)
                    obj.save()
                else:
                    return render(request,'stock_transaction.html',locals())

                h = request.user.hold_set.filter(number = int(request.POST['stockcode']))
                if h:
                   
                    h[0].amount = h[0].amount + int(request.POST['amount'])
                    h[0].save()
                else:
                    dic = {'number':int(request.POST['stockcode']),'amount':int(request.POST['amount']),'user':request.user}
                    obj = Hold(**dic)
                    obj.save()
                    
            elif request.POST['cmdType'] == 'sell':
                if Stock.objects.filter(number = int(request.POST['stockcode'])):
                    figure = 0 - int(request.POST['amount']) * float(stock_company(int(request.POST['stockcode'])).price[0])
                    user = User.objects.get(username = request.user.username)
                    user.money = user.money - figure
                    user.save()
                    dic = {'genre':1,'number':int(request.POST['stockcode']),'amount':int(request.POST['amount']),'figure':figure,'user':request.user}
                    obj = Deal(**dic)
                    obj.save()
                else:
                    return render(request,'stock_transaction.html',locals())

                h = request.user.hold_set.filter(number = int(request.POST['stockcode']))
                if h:
                   
                    h[0].amount = h[0].amount - int(request.POST['amount'])
                    h[0].save()
                else:
                    return render(request,'stock_transaction.html',locals())
        else:
            return render(request,'stock_transaction.html',locals())
    except Exception as e:
        print(e)
    return render(request,'stock_transaction.html',locals())

# 注销
def do_logout(request):
    try:
        # 直接用django提供的注销功能即可
        logout(request)
    except Exception as e:
        print(e)
    return redirect(request.META.get('HTTP_REFERER','/login/'))


# 注册

def do_reg(request):
    try:
        # 注册一定要以post方式提交
        if request.method == 'POST':
            # 直接使用django的表单类别，否则你还不如去用flask这些轻量级框架
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                # 注册
                user = User.objects.create(
                    username=reg_form.cleaned_data["username"],
                    email=reg_form.cleaned_data["email"],
                    gender=reg_form.cleaned_data["gender"],
                    age=reg_form.cleaned_data["age"],
                    profession=reg_form.cleaned_data["profession"],
                    qq=reg_form.cleaned_data["qq"],
                    mobile=reg_form.cleaned_data["mobile"],
                    # 用户明文提交，不过我们是以加密形式保存密码，就用django提供的密码加密方法，这里用它默认的加密方式
                    password=make_password(reg_form.cleaned_data["password"]),)
                user.save()

                # 注册完之后就登录
                user.backend = \
                    'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
                # 这个登录方法也是django提供的标准方法
                login(request, user)
                # 登录之后跳转回之前的网页
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html',
                    {'reason': reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        print(e)
    return render(request, 'register.html', locals())

# 登录


def do_login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                # 使用django提供的验证方法，传入用户名和密码，会返回一个user对象。这个方法我们也可以重写
                user = authenticate(username=username, password=password)
                # 如果用户存在，那就通过登录验证，和注册一样
                if user is not None:
                    user.backend = \
                        'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
                    login(request, user)
                    print(request.POST.get('source_url'))
                    return redirect(request.POST.get('source_url'))
                # 否则就跳转到登录失败
                else:
                    return render(request, 'failure.html',
                        {'reason': '登录验证失败'})          
            else:
                return render(request, 'failure.html', {'reason': login_form.errors})
        # 如果不是post提交就跳转到登录页面
        else:
            login_form = LoginForm()
    except Exception as e:
        print(e)
    return render(request, 'login.html', locals())
