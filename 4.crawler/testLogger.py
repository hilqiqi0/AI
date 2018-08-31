# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:06:15 2018

@author: Python
"""

import logging
import sys
# 获取logger的实例
logger = logging.getLogger("testLogger")

# 指定logger的输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# 文件日志，终端日志对象
file_handler = logging.FileHandler("testLogger.log")
# 文件日志按照指定的格式来写
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stdout)
# 终端日志按照指定的格式来写
console_handler.setFormatter(formatter)

# 可以设置日志的级别
logger.setLevel(logging.INFO)

# 把文件日志，终端日志对象添加到日志处理器logger中
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.critical("test critical in log")
logger.error("test error in log")
logger.warning("test warning in log")
logger.info("test info in log")
logger.debug("test debug in log")

# 不用的时候，将日志的hanlder移除
#否则会常驻内存
logger.removeHandler(file_handler)
logger.removeHandler(console_handler)









