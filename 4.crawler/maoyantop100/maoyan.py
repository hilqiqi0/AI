# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:51:44 2018

@author: Administrator
"""
import requests
import re
import json
from multiprocessing import Pool
from multiprocessing import Manager
import time
import functools #函数的包装器
import myPymysql # 使用我们自身封装DBHelper来实现数据库的插入操作
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger("maoyan")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler = logging.FileHandler("maoyan.log")
file_handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

# 抓取猫眼TOP100的数据
# 第一步：下载页面
def get_one_page(url):
    # 设置UA
    ua_header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/53"}
    response = requests.get(url, headers=ua_header)
    if response.status_code == 200:#OK
       return response.text
    return None


# 第二步：提取信息
def parse_one_page(html):
    # 使用正则表达式的懒惰+findall的模式来提取信息
    pattern = re.compile('<p class="name"[\s\S]*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern, html)
    
    # 使用yield来返回信息给上层
    for item in items:
        yield{
              "title":item[0].strip(),
              "actor":item[1].strip(),
              "time":item[2].strip()
        }

# 第三步：保存到本地文件系统中
def write_to_file(item):
    # 存储成json格式，以便于将来能方便的提取出来
    with open("maoyanTop100.txt", 'a', encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False)+'\n')

def write_to_sql(item):
    # 创建数据库对象
    dbhelper = myPymysql.DBHelper()
    title = item["title"]
    actor = item["actor"]
    time = item["time"]
    sql = "INSERT INTO testdb.maoyan(title, actor, time)VALUES(%s,%s,%s);"
    params = (title,actor,time)
    result = dbhelper.execute(sql, params)
    if result == True:
        print("插入成功")
    else:
        logger.error("execute: "+sql)
        logger.error("params: "+params)
        print("插入失败")


#0-100: 0,10,20,...,90
#http://maoyan.com/board/4?offset=90
def CrawlPage(lock, offset):
# 将下载页面，解析页面及保存信息放入一个函数中
    url = "http://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)    
    for item in parse_one_page(html):
        lock.acquire() #加锁
        write_to_sql(item) 
        lock.release() #释放锁
#    #url = "http://maoyan.com/board/4?offset="
#    for i in range(minPage,maxPage,step):
#        # 每次生成一个入口的URL
    time.sleep(1)
    
def analysis():
    # 查询分析一下当前一百部电影各个国家的占比
    dbhelper = myPymysql.DBHelper()
    total = dbhelper.fetchCount("SELECT count(*) FROM testdb.maoyan")
    Am = dbhelper.fetchCount("SELECT count(*) FROM testdb.maoyan where time like'%美国%'")
    Ch = dbhelper.fetchCount("SELECT count(*) FROM testdb.maoyan where time like'%中国%'")
    Jp = dbhelper.fetchCount("SELECT count(*) FROM testdb.maoyan where time like'%日本%'")
    Other = total-Am-Ch-Jp
    sizes = Am,Ch,Jp,Other
    labels = 'America','China','Japan','Other'
    colors = 'Green','Red','Yellow','Blue'
    plt.pie(sizes,labels=labels,colors=colors)
    plt.show()

minPage = 0        
maxPage = 100
step =  10        
if __name__ == "__main__":
    # # 使用进程池来抓取数据
    # # 在进程池之间通信或者加锁时需要用Manager
    # manager = Manager()
    # lock = manager.Lock()
    # # 产生一个新的包装函数
    # newCrawlPage = functools.partial(CrawlPage, lock)
    
    # pool = Pool()
    # pool.map(newCrawlPage, [i*10 for i in range(10)])
    # pool.close()
    # pool.join()

    # 数据分析结果
    analysis()

    
logger.removeHandler(file_handler)
        
