# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 09:29:07 2018

@author: Administrator
"""
import os
import hashlib
from multiprocessing import Pool
from multiprocessing import Manager

def innerCopyFile(fileName, srcPath, destPath, q):
    """
    拷贝一个文件
    """
    # 拼出源文件的绝对路径和目标文件的绝对路径
    srcFileName = srcPath+'/'+fileName
    destFileName = destPath+'/'+fileName
    
    # 打开源文件，写入到目标文件
    with open(srcFileName, 'rb') as fr:
        with open(destFileName, 'wb') as fw:
            for i in fr:
                fw.write(i)
    q.put(fileName) # 向进程池的队列中
                    # 放入当前拷贝完成的文件名
                
    return True
#copyFile("httpserver.png", "httpserver2.png")

def copyFile(fileName, srcPath, destPath, q):
    # 如果源文件夹不存在,则报错，然后退出操作
    if not os.path.exists(srcPath):
       print("strPath %s is not exists."%srcPath)
       return None
    
    # 如果目标文件夹不存在，则创建一个文件夹
    if not os.path.exists(destPath):
        try:
            os.mkdir(destPath)
        except:
            print("mkdir %s error"%destPath)
            return None
    
    # 真正的拷贝文件操作
    return innerCopyFile(fileName, srcPath,
                         destPath, q)

CHUCKSIZE = 4096
def hashFile(fileName):
    h = hashlib.sha256()
    with open(fileName, 'rb') as f:
        while True:
            chunk = f.read(CHUCKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    # 接受用户输入的文件目录，同时产生一个副本目录
    srcPath = input("请输入您要拷贝的文件目录:")
    destPath = srcPath+"-副本"
    
    # 如果目标文件夹已经存在的情况下，怎么处理，
    # 注意这里不能覆盖
    while os.path.isdir(destPath):
        destPath = destPath+"-副本"
        
    # 如果源文件夹不存在,则报错，然后退出操作
    if not os.path.exists(srcPath):
       print("strPath %s is not exists."%srcPath)
    
    # 如果目标文件夹不存在，则创建一个文件夹
    if not os.path.exists(destPath):
        try:
            os.mkdir(destPath)
        except:
            print("mkdir %s error"%destPath)   
        
    # 记录当前需要拷贝的文件夹下的文件及其个数
    allFileNames = os.listdir(srcPath)
    allNum = len(allFileNames)
    num = 0# 记录当前完成拷贝的文件个数
    
    # 创建进程池
    p = Pool()
    q = Manager().Queue() #进程池通信需要的队列
    
    # 拷贝文件夹的操作
    for i in allFileNames:
        p.apply_async(func=copyFile, args=(i, srcPath, destPath, q) )    
    p.close()
    
    while num < allNum:
        fileName = q.get() # 如果get不到信息，这里会阻塞
        
        num += 1
        rate = num/allNum*100 #获取当前的进度
        
        # 做文件的HASH值检验
        srcFileName = srcPath+'/'+fileName
        destFileName = destPath+'/'+fileName
        
        if (hashFile(srcFileName) == hashFile(destFileName)):
            print("%s copied ok"%srcFileName)
        else:
            print("%s copied failed"%srcFileName)
        
        print("Current rate is %.1f%%"%rate)
    
    # 等待进程池的操作
    p.join()
    print("Copy Files Done")
    
    