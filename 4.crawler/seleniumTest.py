# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 16:25:08 2018

@author: Python
"""

from selenium import webdriver
import time
#url = "http://www.sina.com.cn"
#browser = webdriver.Chrome()
#browser.get(url)


# 此函数用于打开浏览器
browser = webdriver.Chrome()
#url = "http://index.baidu.com/"#百度指数网站   
#browser.get(url)

def LoginBaidIndex(browser):
    #global browser
    url = "http://index.baidu.com/"#百度指数网站   
    browser.get(url)
    # 点击网页的登录按钮              
    browser.find_element_by_xpath('//*[@id="home"]/div[1]/div[2]/div[1]/div[4]/span/span').click()
    time.sleep(1)
    #传入账号密码
    account="XXXX"
    passwd="YYYY"
    try:
        browser.find_element_by_id("TANGRAM__PSP_14__userName").send_keys(account)
        browser.find_element_by_id("TANGRAM__PSP_14__password").send_keys(passwd)
        browser.find_element_by_id("TANGRAM__PSP_14__submit").click()
    except:
        browser.find_element_by_id("TANGRAM_12__password").send_keys(account)
        browser.find_element_by_id("TANGRAM_12__userName").send_keys(passwd)
        browser.find_element_by_id("TANGRAM_12__submit").click()
    time.sleep(3)

def deal(browser,name):
    # 清空网页输入框
    browser.find_element_by_xpath('//*[@id="search-input-form"]/input[3]').clear()
    # 写入需要搜索的百度指数
    browser.find_element_by_xpath('//*[@id="search-input-form"]/input[3]').send_keys(name)
    # 点击搜索
    try:
        browser.find_element_by_xpath('//*[@id="home"]/div[2]/div[2]/div/div[1]/div/div[2]/div/span/span').click()
    except:
        browser.find_element_by_id("schsubmit").click()
    time.sleep(2)
    #  滚动操作
    browser.execute_script("window.scrollTo(0,1000)") # 执行滚屏操作
    browser.save_screenshot("baiduIndex.png")           # 由于这里图片数据无法直接抓取，所以先截图保存

#LoginBaidIndex()
time.sleep(20)
deal(browser,"Python爬虫")



