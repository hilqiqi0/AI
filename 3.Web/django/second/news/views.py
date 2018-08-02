from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index_views(request):
    return HttpResponse('这是news应用中的index视图')

def template_views(request):
    # 1.通过loader加载模板
    t = loader.get_template("01_template.html")
    # 2.将模板渲染成字符串
    html = t.render()
    # 3.将字符串通过HttpResponse进行响应
    return HttpResponse(html)

def render_views(request):
    return render(request,'01_template.html')

def var1_views(request):
    l = ['老舍','莫言','朱自清']
    t = ('冰心','矛盾','张海伦')
    d = {'A':'ANDROID','B':'BEYOND','C':'COUNTRY'}

    dic = {
        'num':1001,
        'str':"Hello World",
        'list':l,
        'tup':t,
        'dic':d,
        'fun':fun(15,18),
        'A':A(),
    }

    t=loader.get_template("02_var.html")
    html = t.render(dic)
    return HttpResponse(html)

def var2_views(request):
    l = ['老舍','莫言','朱自清']
    t = ('冰心','矛盾','张海伦')
    d = {'A':'ANDROID','B':'BEYOND','C':'COUNTRY'}

    dic = {
        'num':1001,
        'str':"Hello World",
        'list':l,
        'tup':t,
        'dic':d,
        'fun':fun(15,18),
        'A':A(),
    }

    return render(request,'02_var.html',dic)



def exer1_views(request):
    book = "背影"
    author = "朱自清"
    publication = "北京大学出版社"
    publiDate = "2015-10-15"
    return render(request,'03_exer.html',locals())


def tag_views(request):
    l = ["朱自清","老舍","冰心","鲁迅"]
    return render(request,'04_tag.html',locals())



def static_views(request):
    return render(request,'05_static.html')

def parent_views(request):
    return render(request,'06_parent.html')

def child_views(request):
    return render(request,'07_child.html')

def name_views(request):
    return render(request,'08_name.html')

def arg_views(request,num1,num2):
    return HttpResponse("参数１:"+num1+",参数２:"+num2)












def fun(a,b):
    return a+b

class A(object):
    a = "Class A -> a"
    def fun(self):
        return "This is A's function"