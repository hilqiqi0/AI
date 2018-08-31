# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:36:36 2018

@author: Python
"""

import collections
import threading
import time
# 双向队列的演示
candle = collections.deque('candle')
# 两个线程，一个从左侧取，一个从右侧取
#要消耗掉这个双向队列中的字符
def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError: #注意这里利用了异常来改变程序的流程
            break
        else:
            print("%s ：%s\n"%( direction,
                              next ))
            time.sleep(0.1)
    print("done %s\n"%direction)
    return

# 起两个线程，一个从左，一个从右
#取deque的数据，看有没有冲突
left = threading.Thread(target=burn, 
                        args = ('left', 
                            candle.popleft)
                        )
                        
right = threading.Thread(target=burn, 
                        args = ('right', 
                            candle.pop)
                        )

left.start()
right.start()

left.join()
right.join()




        








