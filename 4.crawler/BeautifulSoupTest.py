# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:39:46 2018

@author: Administrator
"""
from bs4 import BeautifulSoup
doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is first paragraph <b>one</b></p>',
       '<p id="secondpara" align="blah">This is second paragraph <b>two</b></p>',
       '</html>']
soup = BeautifulSoup(''.join(doc), "html.parser")
#print(soup.prettify())
#print(type(soup.contents[0])) # tag

print(soup.findAll('p', align="blah"))