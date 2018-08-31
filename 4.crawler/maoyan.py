# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:51:44 2018

@author: Administrator
"""
import requests
import re
# 抓取猫眼TOP100的数据
# 第一步：下载页面
#0-100: 0,10,20,...,90
#http://maoyan.com/board/4?offset=90
def get_one_page(url):
    ua_header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/53"}
    response = requests.get(url, headers=ua_header)
    if response.status_code == 200:#OK
       return response.text
    return None


# 第二步：提取信息
def parse_one_page(html):
    pattern = re.compile('<p class="name"[\s\S]*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern, html)
    
    for item in items:
        print(item[0].strip(),item[1].strip(),item[2].strip())

# 第三部：保存到本地文件系统中
if __name__ == "__main__":
    url = "http://maoyan.com/board/4?offset="
    for i in range(0,10,10):
        parse_one_page(get_one_page(url+str(i)))
        
