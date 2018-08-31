# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:34:47 2018

@author: Python
"""

from captcha.image import ImageCaptcha
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

num = ['0','1','2','3','4','5','6','7','8','9']
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPH = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 得到含有4个字母或数字的验证码
def random_captcha_text(size=5,charset=num
                        +alph+ALPH):
    # 返回一个list
    captcha_text = []
    for i in range(size):
        c = random.choice(charset)
        captcha_text.append(c)
    return captcha_text


def gen_captcha_image():
    # 生成验证码图片对象
    image = ImageCaptcha()
    
    # 生成验证码字母数字组合的字符串
    captcha_text = random_captcha_text()
    captcha_text = ''.join(captcha_text)
    
    # 传入字符串,生成一个png的图片
    catpchaInfo = image.generate(captcha_text)
    
    # 打开Image对象，生成验证码的信息和图片
    captcha_image = Image.open(catpchaInfo)
    captcha_image = np.array(captcha_image)
    
    return captcha_text,captcha_image

if __name__ == "__main__":
    # 生成验证码字符及图片信息
    text, image = gen_captcha_image()
    
    # 显示出生成的验证码和图片
    f = plt.figure()
    ax = f.add_subplot(111)
    ax.text(1.1, 1.9, text, ha='center',
            va = 'center')
    plt.imshow(image)
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
