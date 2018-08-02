from django.http import HttpResponse
#编写视图处理函数，一个函数相当于是一个视图
def run_views(request):
    #request主要封装了的是请求的信息
    return HttpResponse('<h1>这是我的第一个DJANGO程序</h1>')


def run1_views(request,num):
    return HttpResponse("传递的参数是:"+num)

def run2_views(request,num1,num2):
    return HttpResponse("参数１:"+num1+",参数２:"+num2)

def show_views(request,name,age):
    return HttpResponse("参数１:"+name+",参数２:"+age)