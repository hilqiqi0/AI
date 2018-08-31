# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:02:40 2018

@author: Administrator
"""
from lxml import etree
xmlStr = """<bookstore>
<book>
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author> 
  <year>2005</year>
  <price>29.99</price>
</book>
<book>
  <title lang="chs">Pythonp爬虫</title>
  <author>Joe</author> 
  <year>2018</year>
  <price>49.99</price>
</book>
</bookstore>
"""

# 根节点
root = etree.fromstring(xmlStr)
#print(root)

elements = root.xpath("//book/title")
#print(elements[0].getparent())
#print(elements[0].text)
#print(elements[1].text)

attrs = root.xpath("//@lang")
print(attrs) 

