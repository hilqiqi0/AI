# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:30:44 2018

@author: Python
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 11:10:59 2018

@author: Administrator
"""
# 使用cookiejar来登录人人网
from http import cookiejar
from urllib import request
from urllib import parse

# 创建一个Cookiejar的对象
cookie = cookiejar.CookieJar()

# 通过HTTPCookieProcessor处理cookie
cookie_handler = request.HTTPCookieProcessor(cookie)

# 构建一个opener
#用一个新的cookie_handler去取代原来的默认http的处理
opener = request.build_opener(cookie_handler)
# 默认UA的设置类似
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")]

# 找到登录的入口
urlLogin = "http://www.renren.com/ajaxLogin/login?1=1"
#urlLogin = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018402230928"

# 登录的用户名和密码
data = {"email":"xxx","password":"yyy"}

# 通过urlencode
data = bytes(parse.urlencode(data),encoding="utf-8")
# 发送一次post请求，生成登录成功之后的cookie
req = request.Request(urlLogin, data=data,method="POST")
response = opener.open(req) # 注意：这里使用的是opener去HTTP请求的

# 获取到cookie之后，打开自己的个人主页
responsemyRenren = opener.open("http://www.renren.com/961482489/profile")

with open("myRenrenFromCookieJar.html","wb") as f:
    f.write(responsemyRenren.read())