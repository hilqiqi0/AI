# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:19:43 2018

@author: Python
"""
from urllib import request, parse
def getTInfo(key):   
    # 通过抓包的方式获取的url，并不是浏览器上显示的url
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    # 这里的headers及formdata是从浏览器中获取到的
    headers = {
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With" : "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        }
    formdata = {
    "i":key,#key是参数传递进来的
    "from":"auto",
    "to":"auto",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1511219405946",
    "sign":"f8965f67a1d3eee8a69ddf8ccc5f582b",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false"
    }
    
    # 做一次urlencode
    data=bytes(parse.urlencode(formdata),encoding='utf-8')
    #利用Request将headers，dict，data整合成一个对象传入urlopen
    req = request.Request(url,data,headers,method='POST')
    response = request.urlopen(req)
    info = response.read().decode('utf-8') # 这里需要做一次utf-8转码
    # 因为这里需要对信息做文本的处理

    # 使用正则表达式提取翻译出的信息
    strRule = re.compile('"tgt":(.*?)}')
    info2 = strRule.findall(info)
    for i in info2:
               i = i.replace('"',"")
    return info2[0]

if __name__ == "__main__":
    info = input("请输入请要翻译的英文单词:")
    print(getTInfo(info))





