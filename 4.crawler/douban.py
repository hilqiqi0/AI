# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:43:06 2018

@author: Python
"""
from urllib import request
from urllib import error
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
from multiprocessing import Manager
import time
def getHtml(url, ua_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko',
            num_retries=5):
    headers = {"User-Agent":ua_agent}
    req = request.Request(url, headers=headers)
    html = None
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
    except error.URLError or error.HTTPError as e:
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                getHtml(url, ua_agent, num_retries-1)
    return html    

def get_movie_all(html):
    """
    获取当前页面中所有的电影的列表信息
    """
    soup = BeautifulSoup(html, "html.parser")
    movie_list = soup.find_all('div', class_='bd doulist-subject')
    #print(movie_list)
    return movie_list

def get_movie_one(movie):
    """
    获取一部电影的精细信息，最终拼成一个大的字符串
    """
    result = ""
    soup = BeautifulSoup(str(movie),"html.parser")
    title = soup.find_all('div', class_="title")
    soup_title = BeautifulSoup(str(title[0]), "html.parser")
    for line in soup_title.stripped_strings:
        result += line
    
    try:
        score = soup.find_all('span', class_='rating_nums')
        score_ = BeautifulSoup(str(score[0]), "html.parser")
        for line in score_.stripped_strings:
            result += "|| 评分："
            result += line
    except:
         result += "|| 评分：5.0"
         
    abstract = soup.find_all('div', class_='abstract')
    abstract_info = BeautifulSoup(str(abstract[0]), "html.parser")
    for line in abstract_info.stripped_strings:
        result += "|| "
        result += line    
    
    result += '\n'
    return result

def save_file(text,fileName):
    with open(fileName,'ab') as f:
        f.write(text.encode())

def CrawlInfo(url, q):
    # 获取当前节点的信息
    html = getHtml(url)
    movie_list = get_movie_all(html)
    for movie in movie_list:
        result = get_movie_one(movie)
        
        text = '\t'+"电影名:"+str(result)
        save_file(text, "豆瓣2016电影.txt")
        time.sleep(1)
    q.put(url) # 当前的URL处理完成，通知主进程

if __name__ == "__main__":   
    # 使用进程池
    pool = Pool()
    q = Manager().Queue()
    
    # 注意：这里由于只在主进程进行url的匹配，
    #所以，需要保证页面url的全面性，
    #这里的seedUrl选择比较特别
    seedUrl="https://www.douban.com/doulist/3516235/?start=200&sort=seq&sub_type="
    # 当前页的处理
    CrawlInfo(seedUrl, q)
    # 使用正则提取有可能进入待爬队列的URL
    htmlInfo = getHtml(seedUrl)
    pattern = re.compile('(https://www.douban.com/doulist/3516235/\?start=.*)"')
    itemUrls = re.findall(pattern, htmlInfo)
    
    # 队列的方式来模拟广度优先遍历
    crawl_queue = []   #待爬队列
    crawled_queue = [] #已爬队列
    for itemUrl in itemUrls:
        # 在已爬队列中做去重处理
        if itemUrl not in crawled_queue:
            # 在已爬队列中没有的话，则插入待爬队列中
            crawl_queue.append(itemUrl)
    # 在待爬队列中再做一次去重
    crawl_queue = list(set(crawl_queue))
        
    # 抓取队列中的信息为空，则退出循环
    while crawl_queue:
        url = crawl_queue.pop(0)
        # 用进程池中的进程来处理这个URL
        pool.apply_async(func=CrawlInfo, args=(url, q))
        
        # 处理完之后，需要把这个url放入已爬队列中
        url = q.get()
        crawled_queue.append(url)
    pool.close()
    pool.join()
        
    
    
    
    
    
    