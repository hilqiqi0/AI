# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:04:33 2018

@author: Python
"""

# -*- coding:utf-8 -*-
#!/usr/bin/env python3
import time
import os
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import pymongo
#from pymongo import MongoClient
import hashlib
from collections import deque
from lxml import etree
import threading

# 数据库的准备，这里用的是mongodb；
#client = MongoClient('localhost',27017)
#db = client.test
#followers = db.followers

# 注意：这里如果不设置user-agent，可能是无法跳转的
user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)
##dcap = dict(DesiredCapabilities.PHANTOMJS)
##dcap["phantomjs.page.settings.userAgent"] = user_agent
dcap = dict(DesiredCapabilities.FIREFOX)
dcap["firefox.page.settings.userAgent"] = user_agent

#browserPath = '/opt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
#browserPath = '/usr/bin/phantomjs'
# 基本参数的一些准备工作
parser = 'html5lib'
domain = "weibo.com"
url_home = "http://" + domain
download_bf = deque()                # 双向队列，用于保证多线程爬取是安全的
cur_queue = deque()
min_mblogs_allowed = 10              # 爬取的阈值设置
max_follow_fans_ratio_allowed = 3


# 这里有两个爬虫，一个爬取微博数据，一个爬取用户数据
weibo_driver = webdriver.Firefox()  # 微博爬虫
weibo_driver.set_window_size(1920, 1200)  # optional
#user_driver = webdriver.Firefox()   # user crawler
#user_driver.set_window_size(1920, 1200)

##weibo_driver = webdriver.PhantomJS(desired_capabilities=dcap)  # 微博爬虫
##weibo_driver.set_window_size(1920, 1200)  # optional
##user_driver = webdriver.PhantomJS(desired_capabilities=dcap)   # user crawler
##user_driver.set_window_size(1920, 1200)

# url入队列，当然，入队列前要先做查重	
def enqueueUrl(url):
    try:
        md5v = hashlib.md5(url).hexdigest()
        if md5v not in download_bf: # 去重
            print(url + ' is added to queue')
            cur_queue.append(url)
            download_bf.append(md5v)
        # else:
            # print 'Skip %s' % (url)
    except ValueError:
        pass

# 队列左端弹出一个值
def dequeuUrl():
    return cur_queue.popleft()

# 到下一页取抓取		
def go_next_page(cur_driver):
    try:
        next_page = cur_driver.find_element_by_xpath('//a[contains(@class, "page next")]').get_attribute('href')
        print('next page is ' + next_page)
        cur_driver.get(next_page)
        time.sleep(3)
        return True
    except Exception:
        print('next page is not found')
        return False

# 登录
def login(current_driver,username, password):  
    current_driver.get(url_home)  #访问目标网页地址
    #bsObj = BeautifulSoup(user_driver.page_source, parser)  #解析目标网页的 Html 源码
    time.sleep(10)

    # 登录
    current_driver.find_element_by_id('loginname').send_keys(username)
    #user_driver.find_element_by_id('password').send_keys(password)
    #user_driver.find_element_by_xpath('//div[contains(@class,"input_wrap ")][0]/input').send_keys(password)
    current_driver.find_element_by_xpath('/回头ml/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[2]/div/input').send_keys(password)
    # 执行 click()
    current_driver.find_element_by_xpath('//div[contains(@class,"login_btn")][1]/a').click()
    time.sleep(8)
    current_driver.save_screenshot("weiboLogin.png")

    #验证码处理
    ##verifyCode = input("Please input verify code:")            
    ##user_driver.find_element_by_xpath('/回头ml/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[3]/div/input').send_keys(verifyCode)
    ##user_driver.find_element_by_xpath('//div[contains(@class,"login_btn")][1]/a').click()
    ##time.sleep(8)
    ##user_driver.save_screenshot("weiboLogin2.png")
    
# 通过xpath尝试获取元素，最多尝试6次    
def get_element_by_xpath(cur_driver, path):
    tried = 0
    while tried < 6:
        html = cur_driver.page_source
        tr = etree.HTML(html)
        elements = tr.xpath(path)
        if len(elements) == 0:
            time.sleep(1)
            continue
        return elements

# 滚屏，保证能抓到数据            
def scroll_to_bottom():
    # 最多尝试 50 次滚屏
    print('scroll down')
    for i in range(0,50):
        # print 'scrolling for the %d time' % (i)
        weibo_driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        html = weibo_driver.page_source
        tr = etree.HTML(html)
        next_page_url = tr.xpath('//a[contains(@class,"page next")]')
        if len(next_page_url) > 0:
            return next_page_url[0].get('href')
        if len(re.findall('点击重新载入', html)) > 0:
            print('scrolling failed, reload it')
            weibo_driver.find_element_by_link_text('点击重新载入').click()
        time.sleep(1)
        
# 提取微博数据
def extract_feed(feeds):
    for i in range(0,20):
    # 只有在抓取微博数据时需要滚屏
        scroll_to_bottom()
        for element in weibo_driver.find_elements_by_class_name('WB_detail'):
            tried = 0
            while tried < 3:
                try:
                    feed = {}
                    feed['time'] = element.find_element_by_xpath('.//div[@class="WB_from S_txt2"]').text
                    feed['content'] = element.find_element_by_class_name('WB_text').text
                    feed['image_names'] = []
                    for image in element.find_elements_by_xpath('.//li[contains(@class,"WB_pic")]/img'):
                        feed['image_names'].append(re.findall('/([^/]+)$', image.get_attribute('src')))
                    feeds.append(feed)
                    print('--------------------')
                    print(feed['time'])
                    print(feed['content'])
                    break
                except Exception:
                    tried += 1
                    time.sleep(1)
        # 微博信息的下一页
        if go_next_page(weibo_driver) is False:
            return feeds
