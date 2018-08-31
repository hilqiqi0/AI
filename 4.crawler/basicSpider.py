# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:23:00 2018

@author: Python
"""
import logging
import sys
import random
from urllib import request
from urllib import error
from urllib import parse
import time
import socket

# 获取logger的实例
logger = logging.getLogger("testLogger")
# 指定logger的输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# 文件日志，终端日志对象
file_handler = logging.FileHandler("testLogger.log")
# 文件日志按照指定的格式来写
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler(sys.stdout)
# 终端日志按照指定的格式来写
console_handler.setFormatter(formatter)
# 可以设置日志的级别
logger.setLevel(logging.DEBUG)
# 把文件日志，终端日志对象添加到日志处理器logger中
logger.addHandler(file_handler)
logger.addHandler(console_handler)


minRangeForProxy = 1
maxRangeForProxy = 10
minSleepTime = 1
maxSleepTime = 3
def downloadHtml(url, headers=[], proxy={},
                 useProxyRate=0,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT, 
                 decodeInfo="utf-8",
                 num_retries=5
                 ):
    """
    这是一个爬取网页数据的函数
    它支持设置HTTP Request Headers，能设置UA；
    它支持代理服务器的设置,
    它支持timeout超时机制
    它支持网页的编码指定
    它支持服务器返回错误的处理
    如果是3XX则Proxy的库会自己跳转
    如果是4XX错误则记录日志
    如果是5XX错误则尝试五次的机会重新获取网页信息
    """
    if random.randint(minRangeForProxy,
                      maxRangeForProxy) > useProxyRate:
        proxy = None #不使用代理服务器
        print("no proxy")
    
    # 创建Proxy Handler
    proxy_handler = request.ProxyHandler(proxy)
    
    # 创建opener
    opener = request.build_opener(proxy_handler)
    
    # 设置http request的headers
    opener.addheaders = headers
    # 把proxy handler安装到urllib库中
    request.install_opener(opener)
    
    # 初始时将html的返回值设置成None，
    #如果成功的返回，则得到想要html信息
    #否则，None值不会发生改变
    html = None
    # 发起请求
    try:
        res = request.urlopen(url,timeout=timeout)
        html = res.read().decode(decodeInfo)
    except UnicodeDecodeError:
        logger.error("UnicodeDecodeError")
    except error.URLError or error.HTTPError as e:
        logger.error("Download Error")
        # 3XX一般是跳转不需要额外处理
        # 如果出现4XX错误:直接记录日志
        if hasattr(e, 'code') and 400 <= e.code < 500:
            logger.error("Client Error")
            return html
        # 如果出现5XX错误:服务器的问题
        if num_retries > 0:
            # 随机休息1-3秒，然后继续获取当前
            time.sleep(random.randint(minSleepTime, maxSleepTime))
            # 如果状态码为500，则重新做一次抓取的过程
            #直到抓取的次数超过最大上限
            if hasattr(e, 'code') and 500 <= e.code < 600:
                html = downloadHtml(url, headers, proxy,
                                    useProxyRate,
                                    timeout, decodeInfo,
                                    num_retries-1)
        
    
    return html
    
# 测试downloadHtml的方法
headers = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")]
proxy_addr = {"http":"394996257:a1jnn6er@116.62.112.142:16816"}
print(downloadHtml("http://www.baidu.com",
             headers = headers,
             proxy=proxy_addr))

#不用的时候，将日志的hanlder移除
#否则会常驻内存
logger.removeHandler(file_handler)
logger.removeHandler(console_handler)
    
    
    
    
    
    
    
    
    