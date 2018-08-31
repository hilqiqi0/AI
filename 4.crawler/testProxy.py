# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:48:29 2018

@author: Python
"""

#用户名：394996257密码：a1jnn6er
#116.62.112.142 	16816
import urllib.request
import re

# 通过监控百度服务器的返回信息来检测代理服务器是否可用
def checkProxy(html):
    pattern = re.compile("<title>百度一下，你就知道</title>")
    title = re.findall(pattern, html)
    if title is None:
        return False
    else:
        return True

def use_http_proxy(proxy_addr, url):
    #构造代理服务器的Handler
    proxyH = urllib.request.ProxyHandler({"http":
                                         proxy_addr})
    # 由这个proxy handler创建出一个HTTP的opener
    opener = urllib.request.build_opener(proxyH,
                                urllib.request.HTTPHandler)
    # 把这个opener装载进urllib中，准备使用
    urllib.request.install_opener(opener)
    # 发起HTTP请求
    res = urllib.request.urlopen(url, timeout=6)
    # 读取信息
    data = res.read().decode("utf-8")
    return data 

if __name__ == "__main__":
    #proxy_addr = "IP Address:Port Number"
    proxy_addr = "394996257:a1jnn6er@116.62.112.142:16816"
    data = use_http_proxy(proxy_addr, "http://www.baidu.com")
    #print(data)
    print(checkProxy(data))
    
    
    
    
    
    
    
    
